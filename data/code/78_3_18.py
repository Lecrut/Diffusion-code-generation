MONTH_MAP = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}

def calculate_month_difference(month1_name, month2_name):
    try:
        month1 = MONTH_MAP[month1_name.lower()]
        month2 = MONTH_MAP[month2_name.lower()]
        return abs(month1 - month2)
    except KeyError:
        return 'Invalid month name'
if __name__ == '__main__':
    result = calculate_month_difference('January', 'March')
    print(result)