import operator
import os
import glob


'''
    Copyright 2019 TheRedSpy15

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''


def main():
    sourceDir = GetDirectory()
    unsortedFiles = GetFiles(sourceDir)
    extensions = GetFilter()
    for extension in extensions:
        SortSource(unsortedFiles, extension, sourceDir)


def GetFilter():
    return input("Enter extensions to sort (CSV): ").replace(" ","").split(",")


def SortSource(files, extension, sourceDir):
    moveAll = False
    for file in files:
        filePath = os.path.realpath(file)
        fileName = os.path.basename(file)
        movingTo = sourceDir + "/" + extension.replace(".","") + "/" + fileName
        if not movingTo == filePath:
            if operator.contains(fileName, extension):
                if not os.path.exists(extension.replace(".","")):
                    os.mkdir(extension.replace(".",""))

                print("Original:", filePath)
                print("Move to:", movingTo)
                choice = input("Move? Yes/No/Yes all: ").capitalize()

                if not moveAll:
                    if choice == "Yes":
                        os.rename(filePath, movingTo)
                    elif choice == "Yes all":
                        moveAll = True
                        os.rename(filePath, movingTo)
                elif moveAll:
                    os.rename(filePath, movingTo)


def GetFiles(directory):
    return glob.glob(directory + '/**/*.*', recursive=True)


def GetDirectory():
    choice = input("Directory to sort (Custom or Current): ").capitalize()
    if choice == "Current":
        return os.path.dirname(os.path.realpath(__file__))
    elif choice == "Custom":
        return input("Directory: ")
    else:
        print ("Not an option")
        exit(0)


if __name__ == "__main__":
    main()
