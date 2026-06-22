def analyze_lengths(len1, len2):
    def validate_numbers(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers.")
    
    validate_numbers(len1, len2)
    
    minimum = min(len1, len2)
    maximum = max(len1, len2)
    difference = abs(len1 - len2)
    
    return (minimum, maximum, difference)

if __name__ == '__main__':
    length1 = 10.5
    length2 = 3.8
    result = analyze_lengths(length1, length2)
    print(result)