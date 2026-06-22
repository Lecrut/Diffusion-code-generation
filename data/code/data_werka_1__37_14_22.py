class StringConcatenator:
    def __init__(self):
        self.result = ""

    def append_string(self, string):
        if not isinstance(string, str):
            raise ValueError("Input must be a string")
        self.result += string

    def get_result(self):
        return self.result

if __name__ == '__main__':
    string1 = "Hello"
    string2 = "World"
    
    try:
        concatenator = StringConcatenator()
        concatenator.append_string(string1)
        concatenator.append_string(string2)
        result = concatenator.get_result()
        print(result)
    except ValueError as e:
        print(e)