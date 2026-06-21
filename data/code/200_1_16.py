def process_strings(strings):
    def validate_input(input_list):
        if not all(isinstance(item, str) for item in input_list):
            raise ValueError("All elements must be strings")
    
    validate_input(strings)
    return (s.strip().lower() for s in strings)

if __name__ == '__main__':
    sample_values = ["  Python ", "PROGRAMMING", "  Data Science  ", "Machine LEARNING"]
    processed_values = list(process_strings(sample_values))
    print(processed_values)