def double_characters(s):
    return ''.join((c * 2 for c in s))
if __name__ == '__main__':
    print(double_characters('abc'))