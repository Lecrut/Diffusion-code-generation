def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    if sentence[0].isalpha():
        return sentence[0].upper() + sentence[1:]
    return sentence

def run_tests():
    test_cases = [
        ("hello world", "Hello world"),
        ("  spaced", "  spaced"),
        ("123 numbers", "123 numbers"),
        ("", ""),
        ("A", "A"),
        ("a", "A"),
        ("already Capitalized", "Already Capitalized"),
        ("multiple   spaces", "Multiple   spaces"),
    ]
    
    for input_val, expected in test_cases:
        result = capitalize_first_letter(input_val)
        if result != expected:
            return False
    return True

if __name__ == '__main__':
    test_result = run_tests()
    sample_input = "python scripting language"
    print(capitalize_first_letter(sample_input))
    print(f"Tests passed: {test_result}")