if __name__ == '__main__':
    sample_string = 'Python is awesome'
    
    def validate_input(input_string):
        if not isinstance(input_string, str) or not input_string.strip():
            raise ValueError("Input must be a non-empty string.")
    
    def split_string(input_string):
        validate_input(input_string)
        return input_string.split()
    
    result = split_string(sample_string)
    print(result)