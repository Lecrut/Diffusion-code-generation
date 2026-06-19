class StringProcessor:
    def __init__(self, text):
        self.text = text

    def calculate_length(self):
        return len(self.text)

if __name__ == '__main__':
    sample_text_1 = "Hello World"
    sample_text_2 = "Alibaba Cloud"
    processor_1 = StringProcessor(sample_text_1)
    processor_2 = StringProcessor(sample_text_2)
    length_1 = processor_1.calculate_length()
    length_2 = processor_2.calculate_length()
    print(f"Length of '{sample_text_1}': {length_1}")
    print(f"Length of '{sample_text_2}': {length_2}")