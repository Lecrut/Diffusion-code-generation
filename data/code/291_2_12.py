def compare_lengths(inches1, inches2):
    feet1 = inches1 / 12
    feet2 = inches2 / 12
    if feet1 > feet2:
        return f'{inches1} inches'
    elif feet1 < feet2:
        return f'{inches2} inches'
    else:
        return 'Equal lengths'
if __name__ == '__main__':
    result1 = compare_lengths(36, 48)
    print(result1)
    result2 = compare_lengths(72, 96)
    print(result2)