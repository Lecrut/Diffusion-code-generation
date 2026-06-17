def repeat_action(s: str, n: int) -> str:
    return s * n
if __name__ == '__main__':
    string1 = "abc"
    count1 = 5
    result1 = repeat_action(string1, count1)
    print(f"'{string1}' repeated {count1} times is: '{result1}'")
    string2 = "hello"
    count2 = 10
    result2 = repeat_action(string2, count2)
    print(f"'{string2}' repeated {count2} times is: '{result2}'")
    string3 = "Python"
    count3 = 1
    result3 = repeat_action(string3, count3)
    print(f"'{string3}' repeated {count3} times is: '{result3}'")