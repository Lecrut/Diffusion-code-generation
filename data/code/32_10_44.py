class StringLengthCalculator:
    DEFAULT_STRING = "Alibaba Cloud"
    
    @staticmethod
    def calculate_length(s):
        if not isinstance(s, str):
            raise ValueError("Input must be a string")
        return len(s)
    
if __name__ == '__main__':
    sample_string = "Innovative Solutions"
    print(StringLengthCalculator.calculate_length(sample_string))