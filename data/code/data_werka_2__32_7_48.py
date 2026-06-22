class StringMetrics:
    def __init__(self, input_string):
        self.input_string = input_string

    def total_characters(self):
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
        metrics = StringMetrics(value)
        length = metrics.total_characters()
        print(f"The total character count for '{value}' is {length}.")