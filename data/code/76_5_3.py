import datetime
def calculate_date_difference(date_str1, date_str2):
    date_format = '%m/%d/%Y'
    try:
        date1 = datetime.datetime.strptime(date_str1, date_format)
        date2 = datetime.datetime.strptime(date_str2, date_format)
        difference = abs(date1 - date2).days
        return difference
    except ValueError:
        raise ValueError("Invalid date format. Please use 'MM/DD/YYYY'.")
if __name__ == '__main__':
    date_a = '01/15/2023'
    date_b = '03/20/2023'
    print(f"Difference between {date_a} and {date_b}: {calculate_date_difference(date_a, date_b)} days")
    date_c = '12/31/2022'
    date_d = '01/01/2023'
    print(f"Difference between {date_c} and {date_d}: {calculate_date_difference(date_c, date_d)} days")
    date_e = '10/10/2023'
    date_f = '05/05/2023'
    print(f"Difference between {date_e} and {date_f}: {calculate_date_difference(date_e, date_f)} days")
    try:
        calculate_date_difference('2023-01-01', '2023-01-05')
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_date_difference('15-01-2023', '01/01/2023')
    except ValueError as e:
        print(f"Error caught: {e}")