def repeat_string(substring, n):
    if n <= 0:
        return ""
    return substring * n
if __name__ == '__main__':
    substring = "abc"
    n1 = 3
    result1 = repeat_string(substring, n1)
    print(f"Substring: {substring}, N: {n1}, Result: {result1}")
    substring = "hello"
    n2 = 5
    result2 = repeat_string(substring, n2)
    print(f"Substring: {substring}, N: {n2}, Result: {result2}")
    substring = "test"
    n3 = 0
    result3 = repeat_string(substring, n3)
    print(f"Substring: {substring}, N: {n3}, Result: {result3}")
    substring = "xyz"
    n4 = -2
    result4 = repeat_string(substring, n4)
    print(f"Substring: {substring}, N: {n4}, Result: {result4}")