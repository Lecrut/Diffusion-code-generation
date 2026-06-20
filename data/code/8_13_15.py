def split_comma_string(s):
    for item in s.split(','):
        stripped = item.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    sample = "apple, banana, , cherry,  , date"
    result = list(split_comma_string(sample))
    print(result)