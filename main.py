import json


class MyClass:

    def __init__(self, filepath):
        self.filepath = filepath
        self.jsonObject = {}
        self.keys_to_remove = ["ReplaceColumns", "Rule", "SubCategory"]  # Keys to be deleted.
        self.readFile()

    def readFile(self):
        with open(self.filepath) as jsonFile:
            self.jsonObject = json.load(jsonFile)

    def IncreaseValue(self):
        for p_id, p_info in self.jsonObject.items():
            p_info["SystemID"] += 1

    def SplitFunc(self):
        for p_id, p_info in self.jsonObject.items():
            counter = 1
            for val in (p_info["SubCategory"].split()):
                p_info["SubCategory" + str(counter)] = val
                counter += 1

    def DeleteColoumns(self):
        for p_id, p_info in self.jsonObject.items():
            for key, value in list(
                    p_info.items()):  # List operation avoids RunTime error. Because dict size can not change when program runs.
                if key in self.keys_to_remove:
                    del p_info[key]

    def EmptyValues(self):
        for p_id, p_info in self.jsonObject.items():
            for key, value in list(p_info.items()):
                if not value:
                    del p_info[key]

    def get_output(self):
        for p_id, p_info in self.jsonObject.items():
            print("\nKey: " + p_id)
            for key, value in p_info.items():
                print(key + ": " + str(value))

    # def OutFile(self):

    #     with open(self.filepath,"w") as jsonFile:
    #         json.dump(self.jsonObject, jsonFile)


if __name__ == '__main__':
    x = MyClass("enter your json path")
    x.IncreaseValue()
    x.EmptyValues()
    x.SplitFunc()
    x.DeleteColoumns()
    x.get_output()
    # x.OutFile()
