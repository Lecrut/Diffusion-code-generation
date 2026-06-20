def split_comma_separated(s):
    yield from (part.strip() for part in s.split(',') if part.strip())

if __name__ == '__main__':
    sample = "  apple , banana , ,  cherry  , ,  date  "
    result = split_comma_separated(sample)
    print(list(result))