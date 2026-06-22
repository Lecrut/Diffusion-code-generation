def capitalize_first(s):
    if not s:
        return s
    return s[0].upper() + s[1:]

if __name__ == '__main__':
    sample = "hello world"
    result = capitalize_first(sample)
    print(result)