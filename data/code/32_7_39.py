class StringAnalyzer:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_length(self):
        return len(self.input_string)

if __name__ == '__main__':
    sample_values = [
        "Hello, World!",
        "",
        "!!!",
        "   ",
        "123 ABC!@#"
    ]
    
    for value in sample_values:
        analyzer = StringAnalyzer(value)
        length = analyzer.get_length()
        print(f"The length of '{value}' is {length}.")