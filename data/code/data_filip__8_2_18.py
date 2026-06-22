TOKEN_MAP = {'sep': ',', 'strip': str.strip}

def split_and_strip(source):
    raw_parts = source.split(TOKEN_MAP['sep'])
    return [TOKEN_MAP['strip'](part) for part in raw_parts]

if __name__ == '__main__':
    test_string = "  hello , world ,  foo  , bar  "
    output = split_and_strip(test_string)
    print(output)