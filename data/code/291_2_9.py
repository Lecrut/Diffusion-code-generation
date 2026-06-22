def compare_inches_feet(inches1, inches2, feet1, feet2):
    length_in_inches = inches1 + inches2 / 12
    length_in_feet = feet1 + feet2
    if length_in_inches > length_in_feet:
        return f'{inches1} inches and {inches2} inches'
    elif length_in_inches < length_in_feet:
        return f'{feet1} feet and {feet2} feet'
    else:
        return 'Equal'
if __name__ == '__main__':
    result1 = compare_inches_feet(36, 0, 3, 0)
    print(result1)
    result2 = compare_inches_feet(35, 0, 3, 0)
    print(result2)
    result3 = compare_inches_feet(36, 0, 3, 1)
    print(result3)