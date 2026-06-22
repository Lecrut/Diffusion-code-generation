def get_nth_char(s, n):
    if n >= 0:
        if n < len(s):
            return s[n]
        else:
            return None
    else:
        idx = -n
        if idx <= len(s):
            return s[-idx]
        else:
            return None

if __name__ == '__main__':
    text = "Python"
    index = -3
    result = get_nth_char(text, index)
    print(result)