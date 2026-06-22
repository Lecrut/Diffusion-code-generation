def compare_measures(inches1, feet1, inches2, feet2):
    measure1 = inches1 + feet1 * 12
    measure2 = inches2 + feet2 * 12
    if measure1 > measure2:
        return f'{inches1} inches and {feet1} feet'
    elif measure2 > measure1:
        return f'{inches2} inches and {feet2} feet'
    else:
        return 'Both measures are equal'
if __name__ == '__main__':
    result = compare_measures(36, 0, 48, 1)
    print(result)