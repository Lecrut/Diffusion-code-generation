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
    try:
        concatenator = StringConcatenator()
        sample_string1 = "Hello"
        sample_string2 = "World"
        concatenator.append_string(sample_string1)
        concatenator.append_string(sample_string2)
        result = concatenator.get_result()
        print(result)
    except ValueError as e:
        print(e)