def repeat_action(s: str, n: int) -> str:
    return s * n
if __name__ == '__main__':
    string_to_repeat = "hello"
    repeat_count = 3
    result = repeat_action(string_to_repeat, repeat_count)
    print(result)