def repeat_string(substring, n):
    if n <= 0:
        raise ValueError("N must be a positive integer")
    return substring * n
if __name__ == '__main__':
    sub = "abc"
    count = 3
    try:
        result = repeat_string(sub, count)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    sub2 = "hello"
    count2 = 5
    try:
        result2 = repeat_string(sub2, count2)
        print(result2)
    except ValueError as e:
        print(f"Error: {e}")
    sub3 = "test"
    count3 = 0
    try:
        result3 = repeat_string(sub3, count3)
        print(result3)
    except ValueError as e:
        print(f"Error: {e}")