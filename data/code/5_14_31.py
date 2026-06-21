def compare_lengths(length1_in_inches, length2_in_cm):
    inches_to_cm = 2.54
    length1_in_cm = length1_in_inches * inches_to_cm
    if length1_in_cm > length2_in_cm:
        return f'{length1_in_inches} inches is longer than {length2_in_cm} cm.'
    elif length1_in_cm < length2_in_cm:
        return f'{length2_in_cm} cm is longer than {length1_in_inches} inches.'
    else:
        return 'Both lengths are equal.'
if __name__ == '__main__':
    length1 = 10
    length2 = 25.4
    result = compare_lengths(length1, length2)
    print(result)