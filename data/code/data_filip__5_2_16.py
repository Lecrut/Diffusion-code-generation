def capitalize_first_letter(sentence):
    if not sentence:
        return sentence
    return sentence[0].upper() + sentence[1:]

def run_tests():
    test_cases = [
        ("hello world", "Hello world"),
        ("python is great", "Python is great"),
        ("", ""),
        ("a", "A"),
        ("already Capitalized", "Already Capitalized"),
        ("123 numbers", "123 numbers"),
    ]
    all_passed = True
    for input_str, expected in test_cases:
        result = capitalize_first_letter(input_str)
        if result != expected:
            all_passed = False
            print(f"FAIL: capitalize_first_letter({input_str!r}) = {result!r}, expected {expected!r}")
    return all_passed

if __name__ == '__main__':
    print(capitalize_first_letter("hello world"))
    print(capitalize_first_letter("python programming"))
    print(run_tests())