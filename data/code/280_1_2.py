def repeat_action(s: str, n: int) -> str:
    return s * n
if __name__ == '__main__':
    string_to_repeat = "hello"
    number_of_repeats = 3
    result = repeat_action(string_to_repeat, number_of_repeats)
    print(result)