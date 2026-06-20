def calculate_month_difference(month1_name, month2_name):
    month_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    try:
        month1 = month_map[month1_name.lower()]
        month2 = month_map[month2_name.lower()]
        return abs(month1 - month2)
    except KeyError:
        raise ValueError('Invalid month name')
if __name__ == '__main__':
    print(calculate_month_difference('january', 'march'))
    print(calculate_month_difference('december', 'february'))