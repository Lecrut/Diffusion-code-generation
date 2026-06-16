def repeat_string(substring, n):
    if n <= 0:
        return ""
    return substring * n
if __name__ == '__main__':
    substring1 = "abc"
    n1 = 3
    result1 = repeat_string(substring1, n1)
    print(f"'{substring1}' repeated {n1} times is: '{result1}'")
    substring2 = "hello"
    n2 = 5
    result2 = repeat_string(substring2, n2)
    print(f"'{substring2}' repeated {n2} times is: '{result2}'")
    substring3 = "Python"
    n3 = 0
    result3 = repeat_string(substring3, n3)
    print(f"'{substring3}' repeated {n3} times is: '{result3}'")
    substring4 = "test"
    n4 = -2
    result4 = repeat_string(substring4, n4)
    print(f"'{substring4}' repeated {n4} times is: '{result4}'")