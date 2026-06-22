def split_and_filter(s):
    return list(filter(lambda x: x.strip(), s.split(',')))

if __name__ == '__main__':
    result = split_and_filter("a, b, , c, , d,  ")
    print(result)