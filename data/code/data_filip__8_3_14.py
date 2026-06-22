def split_string(s):
    return list(filter(lambda x: x.strip(), s.split(',')))

if __name__ == '__main__':
    result = split_string('a, b, , c,  ,d')
    print(result)