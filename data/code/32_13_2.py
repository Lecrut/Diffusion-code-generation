def get_string_length(s: str) -> int:
    return len(s)

if __name__ == '__main__':
    test_cases = ["hello", "", "Python is awesome!", "\n\t "]
    print([(s, get_string_length(s)) for s in test_cases])