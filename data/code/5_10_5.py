def difference_length(len1, len2):
    return len1 - len2 if len1 >= len2 else len2 - len1

if __name__ == '__main__':
    length_a = 10
    length_b = 7
    print(difference_length(length_a, length_b))
    length_c = 3
    length_d = 15
    print(difference_length(length_c, length_d))