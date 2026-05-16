import datetime
def calculate_month_difference(month1_str, month2_str):
    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    if month1_str not in month_map or month2_str not in month_map:
        raise ValueError("Invalid month string provided")
    month1 = month_map[month1_str]
    month2 = month_map[month2_str]
    return abs(month1 - month2)
if __name__ == '__main__':
    month_a = 'January'
    month_b = 'March'
    difference1 = calculate_month_difference(month_a, month_b)
    print(f"Difference between {month_a} and {month_b}: {difference1}")
    month_c = 'December'
    month_d = 'June'
    difference2 = calculate_month_difference(month_c, month_d)
    print(f"Difference between {month_c} and {month_d}: {difference2}")
    month_e = 'July'
    month_f = 'July'
    difference3 = calculate_month_difference(month_e, month_f)
    print(f"Difference between {month_e} and {month_f}: {difference3}")