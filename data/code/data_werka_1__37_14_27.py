class StringAccumulator:
    def __init__(self):
        self._result = ""

    def add_string(self, string):
        if not isinstance(string, str):
            raise ValueError("Input must be a string")
        self._result += string

    def get_concatenated_result(self):
        return self._result

if __name__ == '__main__':
    accumulator = StringAccumulator()
    sample_string1 = "Hello"
    sample_string2 = "World"
    
    accumulator.add_string(sample_string1)
    accumulator.add_string(" ")
    accumulator.add_string(sample_string2)
    
    print(accumulator.get_concatenated_result())