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
        concatenator.append_string("Hello")
        concatenator.append_string("World")
        result = concatenator.get_result()
        print(result)
    except ValueError as e:
        print(e)