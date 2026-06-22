class StringManipulator:
    def __init__(self):
        self.internal_strings = {"string1": "", "string2": ""}
    
    def set_string(self, key, value):
        if key in self.internal_strings:
            self.internal_strings[key] = value
    
    def combine_strings(self):
        return self.internal_strings["string1"] + self.internal_strings["string2"]

if __name__ == '__main__':
    manipulator = StringManipulator()
    manipulator.set_string("string1", "Hello")
    manipulator.set_string("string2", "World")
    result = manipulator.combine_strings()
    print(result)