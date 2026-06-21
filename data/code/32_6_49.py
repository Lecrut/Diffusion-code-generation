class StringAnalyzer:
    @staticmethod
    def calculate_length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_strings = {
        "greeting": "Hello, World!",
        "example": "Example String",
        "company": "Alibaba Cloud"
    }
    
    for key, value in sample_strings.items():
        try:
            length = StringAnalyzer.calculate_length(value)
            print(f"Length of '{key}': {length}")
        except ValueError as e:
            print(e)