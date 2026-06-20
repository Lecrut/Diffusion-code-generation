def compare_lengths(len1, len2):
    if len1 < len2:
        return (len1, len2)
    else:
        return (len2, len1)

if __name__ == '__main__':
    result = compare_lengths(10, 25)
    print(result)