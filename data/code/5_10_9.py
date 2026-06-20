def length_difference(len1, len2):
    return len1 - len2 if len1 >= len2 else len2 - len1

if __name__ == '__main__':
    print(length_difference(10, 5))
    print(length_difference(5, 10))
    print(length_difference(7, 7))