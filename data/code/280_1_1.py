def repeat_action(s: str, n: int) -> str:
    if n <= 0:
        return ""
    return s * n
if __name__ == '__main__':
    string1 = "hello"
    number1 = 3
    result1 = repeat_action(string1, number1)
    print(f"'{string1}' repeated {number1} times: '{result1}'")
    string2 = "abc"
    number2 = 5
    result2 = repeat_action(string2, number2)
    print(f"'{string2}' repeated {number2} times: '{result2}'")
    string3 = "Python"
    number3 = 0
    result3 = repeat_action(string3, number3)
    print(f"'{string3}' repeated {number3} times: '{result3}'")
    string4 = ""
    number4 = 10
    result4 = repeat_action(string4, number4)
    print(f"'{string4}' repeated {number4} times: '{result4}'")