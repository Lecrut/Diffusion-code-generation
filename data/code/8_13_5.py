def split_non_empty_stripped(s):
    for item in s.split(','):
        stripped = item.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample = "  hello , , world ,  python  ,  "
    result = list(split_non_empty_stripped(sample))
    print(result)