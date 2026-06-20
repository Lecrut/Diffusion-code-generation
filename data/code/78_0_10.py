MONTH_NAMES = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

def calculate_month_difference(month1_name, month2_name):
    if month1_name not in MONTH_NAMES or month2_name not in MONTH_NAMES:
        raise ValueError('Invalid month name provided.')
    month1 = MONTH_NAMES[month1_name.lower()]
    month2 = MONTH_NAMES[month2_name.lower()]
    difference = abs(month1 - month2)
    return difference
if __name__ == '__main__':
    month_a = 'December'
    month_b = 'March'
    try:
        diff = calculate_month_difference(month_a, month_b)
        print(diff)
    except ValueError as e:
        print(e)