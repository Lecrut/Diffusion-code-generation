def compare_measures(inches1, feet1, inches2, feet2):
    total_inches1 = inches1 + feet1 * 12
    total_inches2 = inches2 + feet2 * 12
    if total_inches1 > total_inches2:
        return f'{inches1} inches and {feet1} feet'
    elif total_inches2 > total_inches1:
        return f'{inches2} inches and {feet2} feet'
    else:
        return 'Both measures are equal'
if __name__ == '__main__':
    print(compare_measures(3, 0, 4, 1))
    print(compare_measures(6, 2, 5, 3))
    print(compare_measures(12, 1, 12, 1))