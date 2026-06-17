def repeat_action(s: str, n: int) -> str:
    return s * n
if __name__ == '__main__':
    test_string = "abc"
    test_repetitions = 5
    result = repeat_action(test_string, test_repetitions)
    print(result)