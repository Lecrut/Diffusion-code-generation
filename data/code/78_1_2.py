from datetime import datetime
def calculate_month_difference(month1_str, month2_str):
    month_map = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4,
        'May': 5, 'June': 6, 'July': 7, 'August': 8,
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    try:
        month1 = month_map[month1_str]
        month2 = month_map[month2_str]
        return abs(month1 - month2)
    except KeyError as e:
        raise ValueError(f"Invalid month string provided: {e}")
if __name__ == '__main__':
    month_a = 'January'
    month_b = 'March'
    difference = calculate_month_difference(month_a, month_b)
    print(f"The difference between {month_a} and {month_b} is: {difference}")
    month_c = 'December'
    month_d = 'June'
    difference2 = calculate_month_difference(month_c, month_d)
    print(f"The difference between {month_c} and {month_d} is: {difference2}")
    month_e = 'May'
    month_f = 'May'
    difference3 = calculate_month_difference(month_e, month_f)
    print(f"The difference between {month_e} and {month_f} is: {difference3}")