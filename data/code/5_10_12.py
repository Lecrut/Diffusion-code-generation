def difference_length(len1, len2):
    return len1 - len2 if len1 > len2 else len2 - len1

if __name__ == '__main__':
    print(difference_length(10, 4))
    print(difference_length(3, 8))
    print(difference_length(5, 5))