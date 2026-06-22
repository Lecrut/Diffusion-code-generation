def compare_lengths(inches1, feet1, inches2, feet2):
    length1 = inches1 + feet1 * 12
    length2 = inches2 + feet2 * 12
    if length1 > length2:
        return f'{inches1} inches and {feet1} feet'
    elif length2 > length1:
        return f'{inches2} inches and {feet2} feet'
    else:
        return 'Both measures are equal'
if __name__ == '__main__':
    print(compare_lengths(36, 0, 48, 0))
    print(compare_lengths(12, 1, 14, 0))
    print(compare_lengths(24, 0, 24, 0))