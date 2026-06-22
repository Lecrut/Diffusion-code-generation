def trim_whitespace(strings):
    return [s.strip() for s in strings]

if __name__ == '__main__':
    data = ["  hello  ", "world ", "  python ", "  "]
    result = trim_whitespace(data)
    print(result)