def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

def run_tests():
    test_cases = [
        ("", ""),
        ("a", "A"),
        ("hello", "Hello"),
        ("world", "World"),
        ("hello world", "Hello world"),
        ("123abc", "123abc"),
        ("  spaces", "  spaces"),
        ("already Capitalized", "Already Capitalized"),
    ]
    
    results = []
    for i, (input_str, expected) in enumerate(test_cases):
        result = capitalize_first_letter(input_str)
        passed = result == expected
        results.append((i, passed, input_str, expected, result))
    
    return results

if __name__ == '__main__':
    test_results = run_tests()
    for idx, passed, input_str, expected, actual in test_results:
        status = "PASS" if passed else "FAIL"
        print(f"Test {idx}: {status} | Input: '{input_str}' | Expected: '{expected}' | Actual: '{actual}'")
    
    sample_sentences = [
        "the quick brown fox",
        "jumps over the lazy dog",
        "python programming",
        "machine learning basics",
        ""
    ]
    
    for sentence in sample_sentences:
        capitalized = capitalize_first_letter(sentence)
        print(capitalized)