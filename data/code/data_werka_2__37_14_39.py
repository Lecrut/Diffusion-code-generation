class StringConcatenator:
    def __init__(self):
        self.result = ""

    def append(self, string):
        if not isinstance(string, str):
            raise ValueError("Input must be a string")
        self.result += string

    def get_concatenated_result(self):
        return self.result

if __name__ == '__main__':
    STRING1 = "Hello"
    STRING2 = "World"
    
    concatenator = StringConcatenator()
    concatenator.append(STRING1)
    concatenator.append(" ")
    concatenator.append(STRING2)
    
    result = concatenator.get_concatenated_result()
    print(result)