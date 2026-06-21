class StringMetrics:
    @staticmethod
    def calculate_length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)

if __name__ == '__main__':
    sample_texts = {
        "greeting": "Hello, World!",
        "example": "Example String",
        "cloud_service": "Alibaba Cloud AI"
    }
    
    for description, text in sample_texts.items():
        try:
            length = StringMetrics.calculate_length(text)
            print(f"Length of '{description}': {length}")
        except ValueError as e:
            print(e)