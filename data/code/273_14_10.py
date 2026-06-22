def repeat_characters(s):
    return ''.join((c * 2 for c in s))
if __name__ == '__main__':
    print(repeat_characters('abc'))