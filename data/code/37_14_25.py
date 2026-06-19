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
    sample_values = {
        "greeting": "Hello",
        "farewell": "World"
    }
    
    concatenator = StringConcatenator()
    concatenator.append_string(sample_values["greeting"])
    concatenator.append_string(" ")
    concatenator.append_string(sample_values["farewell"])
    result = concatenator.get_result()
    print(result)