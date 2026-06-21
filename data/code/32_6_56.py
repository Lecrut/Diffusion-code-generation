class StringAnalyzer:
    @staticmethod
    def check_input_type(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")

    @staticmethod
    def calculate_length(s):
        StringAnalyzer.check_input_type(s)
        return len(s)

if __name__ == '__main__':
    sample_string1 = "Welcome to Alibaba Cloud"
    sample_string2 = "Innovate and Transform"
    
    try:
        length1 = StringAnalyzer.calculate_length(sample_string1)
        print(f"Length of '{sample_string1}': {length1}")
        
        length2 = StringAnalyzer.calculate_length(sample_string2)
        print(f"Length of '{sample_string2}': {length2}")
    except ValueError as e:
        print(e)