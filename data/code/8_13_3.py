def split_non_empty_stripped(s):
    parts = s.split(',')
    for part in parts:
        stripped = part.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample = " apple , , banana , cherry , , date "
    result = list(split_non_empty_stripped(sample))
    print(result)