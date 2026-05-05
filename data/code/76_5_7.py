import datetime
def calculate_date_difference(date_str1, date_str2):
    date_format = '%m/%d/%Y'
    try:
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        difference = abs(date1 - date2).days
        return difference
    except ValueError:
        raise ValueError("Invalid date format. Please use MM/DD/YYYY.")
if __name__ == '__main__':
    date_a = '01/15/2023'
    date_b = '03/20/2023'
    date_c = '12/31/2022'
    date_d = '02/01/2023'
    invalid_date_1 = '2023-01-15'
    invalid_date_2 = '30/02/2023'
    try:
        diff1 = calculate_date_difference(date_a, date_b)
        print(f"Difference between {date_a} and {date_b}: {diff1} days")
    except ValueError as e:
        print(f"Error for sample 1: {e}")
    try:
        diff2 = calculate_date_difference(date_c, date_d)
        print(f"Difference between {date_c} and {date_d}: {diff2} days")
    except ValueError as e:
        print(f"Error for sample 2: {e}")
    try:
        calculate_date_difference(date_a, invalid_date_1)
    except ValueError as e:
        print(f"Error for invalid date 1: {e}")
    try:
        calculate_date_difference(invalid_date_2, date_a)
    except ValueError as e:
        print(f"Error for invalid date 2: {e}")