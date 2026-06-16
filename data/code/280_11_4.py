def repeat_action(s: str, n: int) -> str:
    return s * n
if __name__ == '__main__':
    string_to_repeat = "abc"
    repetitions = 1000000
    result = repeat_action(string_to_repeat, repetitions)
    print(result)