def split_non_empty_stripped(s):
    return (item.strip() for item in s.split(',') if item.strip())

if __name__ == '__main__':
    sample = "  hello , world , , foo , bar  "
    result = list(split_non_empty_stripped(sample))
    print(result)