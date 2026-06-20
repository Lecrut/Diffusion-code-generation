def parse_comma_separated(s):
    for item in s.split(','):
        stripped = item.strip()
        if stripped:
            yield stripped

if __name__ == '__main__':
    result = list(parse_comma_separated("apple, , banana, ,  cherry  , "))
    print(result)