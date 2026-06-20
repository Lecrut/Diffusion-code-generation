def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

def run_tests():
    test_cases = [
        ("hello world", "Hello world"),
        ("already capitalized", "Already capitalized"),
        ("", ""),
        ("a", "A"),
        ("   leading spaces", "   Leading spaces"),
        ("123 numbers", "123 numbers"),
        ("MiXeD cAsE", "MiXeD cAsE")
    ]
    
    results = []
    for input_str, expected in test_cases:
        result = capitalize_first_letter(input_str)
        results.append((input_str, expected, result, result == expected))
    
    return results

if __name__ == '__main__':
    test_results = run_tests()
    for input_str, expected, result, passed in test_results:
        print(f"Input: '{input_str}' | Expected: '{expected}' | Got: '{result}' | Passed: {passed}")
    
    sample_sentences = [
        "the quick brown fox jumps over the lazy dog",
        "python is a great programming language",
        "data science and machine learning",
        "artificial intelligence is changing the world"
    ]
    
    for sentence in sample_sentences:
        capitalized = capitalize_first_letter(sentence)
        print(capitalized)