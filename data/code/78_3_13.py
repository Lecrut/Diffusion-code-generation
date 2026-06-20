def is_valid_month_name(month_name):
    valid_months = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'}
    return month_name.lower() in valid_months

def get_month_index(month_name):
    month_map = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12}
    return month_map[month_name.lower()]

def calculate_month_difference(month1_name, month2_name):
    if not is_valid_month_name(month1_name) or not is_valid_month_name(month2_name):
        return 'Invalid month name'
    month1 = get_month_index(month1_name)
    month2 = get_month_index(month2_name)
    if month1 == month2:
        return 0
    elif month1 < month2:
        return month2 - month1
    else:
        return month1 - month2
if __name__ == '__main__':
    print(calculate_month_difference('January', 'March'))
    print(calculate_month_difference('October', 'February'))
    print(calculate_month_difference('December', 'December'))
    print(calculate_month_difference('July', 'April'))