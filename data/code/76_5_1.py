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
    try:
        calculate_date_difference('2023-01-01', '2023-01-02')
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        calculate_date_difference('15-01-2023', '20-01-2023')
    except ValueError as e:
        print(f"Error caught: {e}")