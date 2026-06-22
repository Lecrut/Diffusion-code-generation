class StringCaseConverter:
    def __init__(self, text):
        self.text = text

    def to_lowercase(self):
        return self.text.lower()

    def swap_case(self):
        return self.text.swapcase()

if __name__ == '__main__':
    sample_text = 'Hello World'
    converter = StringCaseConverter(sample_text)
    
    lowercased_text = converter.to_lowercase()
    swapped_case_text = converter.swap_case()
    
    print(lowercased_text)
    print(swapped_case_text)