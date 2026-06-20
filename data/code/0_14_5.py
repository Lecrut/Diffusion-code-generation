def filter_digits(s):
    return [int(ch) for ch in s if ch.isdigit()]

if __name__ == '__main__':
    print(filter_digits("abc123xy4"))