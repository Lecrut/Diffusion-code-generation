def compare_lengths(len1, len2):
    if len1 > len2:
        return (1, len1, len2)
    elif len1 < len2:
        return (-1, len1, len2)
    else:
        return (0, len1, len2)

if __name__ == '__main__':
    print(compare_lengths(5.5, 3.2))
    print(compare_lengths(1.0, 1.0))
    print(compare_lengths(2.0, 4.5))