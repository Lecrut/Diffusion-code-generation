def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse_string(text)

def run_validation_tests():
    test_samples = ["kayak", "Python", "level", "World", "deified"]
    results = []
    for sample in test_samples:
        check_result = is_palindrome(sample)
        results.append((sample, check_result))
    return results

if __name__ == '__main__':
    output_data = run_validation_tests()
    for original_string, result_flag in output_data:
        print(original_string, result_flag)