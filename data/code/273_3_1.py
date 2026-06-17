def repeat_string(substring, n):
    if n <= 0:
        return ""
    if n == 1:
        return substring
    return substring + repeat_string(substring, n - 1)
if __name__ == '__main__':
    sub = "abc"
    count = 3
    result = repeat_string(sub, count)
    print(result)