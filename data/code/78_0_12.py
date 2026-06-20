def calculate_month_difference(month1_name, month2_name):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    if month1_name not in months or month2_name not in months:
        raise ValueError('Invalid month name provided.')
    index1 = months.index(month1_name)
    index2 = months.index(month2_name)
    difference = abs(index1 - index2)
    return difference
if __name__ == '__main__':
    month_a = 'December'
    month_b = 'March'
    try:
        diff = calculate_month_difference(month_a, month_b)
        print(diff)
    except ValueError as e:
        print(e)
    month_c = 'January'
    month_d = 'March'
    try:
        result = calculate_month_difference(month_c, month_d)
        print(result)
    except ValueError as e:
        print(e)
    month_e = 'November'
    month_f = 'December'
    try:
        result = calculate_month_difference(month_e, month_f)
        print(result)
    except ValueError as e:
        print(e)