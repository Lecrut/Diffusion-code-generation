def split_and_filter(text):
    return list(filter(lambda s: s.strip(), text.split(',')))

if __name__ == '__main__':
    result = split_and_filter("apple, , banana, , ,cherry , date")
    print(result)