def parse_comma_separated(s):
    return (item.strip() for item in s.split(',') if item.strip())

if __name__ == '__main__':
    sample_string = " apple , banana, , cherry, , date "
    result = list(parse_comma_separated(sample_string))
    print(result)