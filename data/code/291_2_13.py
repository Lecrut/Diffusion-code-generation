def compare_lengths(inches1, feet1, inches2, feet2):
    length1 = inches1 + feet1 * 12
    length2 = inches2 + feet2 * 12
    if length1 > length2:
        return f"{inches1} inches and {feet1} feet"
    else:
        return f"{inches2} inches and {feet2} feet"

if __name__ == '__main__':
    print(compare_lengths(36, 0, 48, 1))