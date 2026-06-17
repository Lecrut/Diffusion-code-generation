def repeat_string(s: str, n: int) -> str:
    if n <= 0:
        return ""
    return s * n
if __name__ == '__main__':
    string1 = "abc"
    number1 = 3
    result1 = repeat_string(string1, number1)
    print(f"'{string1}' repeated {number1} times is: '{result1}'")
    string2 = "hello"
    number2 = 5
    result2 = repeat_string(string2, number2)
    print(f"'{string2}' repeated {number2} times is: '{result2}'")
    string3 = ""
    number3 = 10
    result3 = repeat_string(string3, number3)
    print(f"'{string3}' repeated {number3} times is: '{result3}'")
    string4 = "a"
    number4 = 0
    result4 = repeat_string(string4, number4)
    print(f"'{string4}' repeated {number4} times is: '{result4}'")