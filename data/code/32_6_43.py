class TextMetrics:
    @staticmethod
    def get_length(text):
        if not isinstance(text, str):
            raise ValueError("Input must be a string")
        return len(text)

if __name__ == '__main__':
    sample_text1 = "Innovative Solutions"
    sample_text2 = "Alibaba Cloud AI"

    try:
        length1 = TextMetrics.get_length(sample_text1)
        print(f"Length of '{sample_text1}': {length1}")

        length2 = TextMetrics.get_length(sample_text2)
        print(f"Length of '{sample_text2}': {length2}")
    except ValueError as e:
        print(e)