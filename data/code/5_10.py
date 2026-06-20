def length_difference(len1, len2):
    return len1 - len2 if len1 > len2 else len2 - len1

if __name__ == '__main__':
    result = length_difference(15, 8)
    print(result)