def capitalize_first(strings):
    result = []
    for s in strings:
        if s:
            result.append(s[0].upper() + s[1:])
        else:
            result.append(s)
    return result

if __name__ == '__main__':
    sample = ["hello", "world", "", "python"]
    print(capitalize_first(sample))