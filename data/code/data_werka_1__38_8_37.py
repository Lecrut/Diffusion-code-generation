def analyze_string(s):
    def validate_input(input_string):
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
    
    def count_characters(input_string):
        char_count = {}
        for char in input_string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
    
    validate_input(s)
    char_count = count_characters(s)
    
    unique_chars = set()
    repeated_chars = []
    
    for char, count in char_count.items():
        if count == 1:
            unique_chars.add(char)
        else:
            repeated_chars.append(char)
    
    return unique_chars, repeated_chars

if __name__ == '__main__':
    sample_string = "example"
    unique, repeated = analyze_string(sample_string)
    print(unique)
    print(repeated)