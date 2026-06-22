def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

def run_tests():
    test_cases = [
        ("hello world", "Hello world"),
        ("python is fun", "Python is fun"),
        ("a single letter", "A single letter"),
        ("", ""),
        ("already Capitalized", "Already capitalized"),
        ("123 numbers first", "123 numbers first"),
        ("   spaces at start", "   spaces at start"),
    ]
    
    results = []
    for input_str, expected in test_cases:
        result = capitalize_first_letter(input_str)
        results.append((input_str, result, expected, result == expected))
    
    return results

if __name__ == '__main__':
    test_results = run_tests()
    for input_str, result, expected, passed in test_results:
        print(f"Input: '{input_str}' -> Result: '{result}' -> Expected: '{expected}' -> Passed: {passed}")