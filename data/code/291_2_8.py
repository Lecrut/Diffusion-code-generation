def compare_lengths(inches1, inches2, feet1, feet2):
    total_inches1 = inches1 + feet1 * 12
    total_inches2 = inches2 + feet2 * 12
    if total_inches1 > total_inches2:
        return f'{inches1} inches and {feet1} feet'
    elif total_inches1 < total_inches2:
        return f'{inches2} inches and {feet2} feet'
    else:
        return 'Both measures are equal'
if __name__ == '__main__':
    result = compare_lengths(3, 5, 1, 2)
    print(result)