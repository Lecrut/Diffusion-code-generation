def validate_repetitions(n: int) -> None:
    if n < 1 or n > 5:
        raise ValueError("Repetitions must be between 1 and 5 inclusive.")

def repeat_action(s: str, n: int) -> str:
    return s * n

if __name__ == '__main__':
    test_string = "abc"
    repetitions = 3
    validate_repetitions(repetitions)
    result = repeat_action(test_string, repetitions)
    print(f"'{test_string}' repeated {repetitions} times is: '{result}'")