class StringUtils:
    @staticmethod
    def _validate_input(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

    @staticmethod
    def compute_length(text):
        StringUtils._validate_input(text)
        return len(text)

if __name__ == '__main__':
    sample_text1 = "Welcome to Alibaba Cloud"
    sample_text2 = "Innovative Solutions"

    try:
        length1 = StringUtils.compute_length(sample_text1)
        print(f"Length of '{sample_text1}': {length1}")
        
        length2 = StringUtils.compute_length(sample_text2)
        print(f"Length of '{sample_text2}': {length2}")
        
    except ValueError as e:
        print(e)