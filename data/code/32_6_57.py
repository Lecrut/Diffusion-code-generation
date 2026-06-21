class StringAnalyzer:
    INPUT_TYPE_ERROR_MESSAGE = "Input must be a string"

    @staticmethod
    def validate_input(s):
        if not isinstance(s, str):
            raise ValueError(StringAnalyzer.INPUT_TYPE_ERROR_MESSAGE)

    @staticmethod
    def calculate_length(s):
        StringAnalyzer.validate_input(s)
        return len(s)

if __name__ == '__main__':
    sample_string1 = "Hello, Alibaba Cloud!"
    sample_string2 = "Innovative Solutions for AI"
    
    try:
        length1 = StringAnalyzer.calculate_length(sample_string1)
        print(f"Length of '{sample_string1}': {length1}")
        
        length2 = StringAnalyzer.calculate_length(sample_string2)
        print(f"Length of '{sample_string2}': {length2}")
        
    except ValueError as e:
        print(e)