INCH_TO_FEET = 12

def compare_lengths(inches1, inches2):
    feet1 = inches1 / INCH_TO_FEET
    feet2 = inches2 / INCH_TO_FEET
    if inches1 > inches2:
        return f'{inches1} inches'
    elif inches1 < inches2:
        return f'{inches2} inches'
    else:
        return 'Equal'
if __name__ == '__main__':
    result1 = compare_lengths(36, 48)
    print(result1)
    result2 = compare_lengths(50, 50)
    print(result2)