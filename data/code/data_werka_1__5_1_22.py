def compare_lengths(length1, length2):
    if length1 > length2:
        return ('greater', length1)
    elif length1 < length2:
        return ('less', length2)
    else:
        return ('equal', length1)

if __name__ == '__main__':
    result = compare_lengths(3.5, 4.2)
    print(result)