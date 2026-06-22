class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string

    def get_first_letter(self):
        if not self.input_string:
            return ""
        return self.input_string[0]

if __name__ == '__main__':
    sample_values = ["Alibaba", "", "Cloud", "Qwen"]
    processors = [StringProcessor(value) for value in sample_values]
    
    results = [processor.get_first_letter() for processor in processors]
    print(results)