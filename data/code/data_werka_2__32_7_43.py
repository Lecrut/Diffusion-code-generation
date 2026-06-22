class StringMetrics:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_total_length(self):
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
        length = metrics.get_total_length()
        print(length)