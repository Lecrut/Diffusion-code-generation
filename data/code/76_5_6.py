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
    date1_str = '01/15/2023'
    date2_str = '03/20/2023'
    try:
        diff = calculate_date_difference(date1_str, date2_str)
        print(diff)
    except ValueError as e:
        print(f"Error: {e}")
    date3_str = '12/31/2022'
    date4_str = '01/01/2023'
    try:
        diff2 = calculate_date_difference(date3_str, date4_str)
        print(diff2)
    except ValueError as e:
        print(f"Error: {e}")
    invalid_date1_str = '2023-01-15'
    date5_str = date2_str
    try:
        diff3 = calculate_date_difference(invalid_date1_str, date5_str)
        print(diff3)
    except ValueError as e:
        print(f"Error: {e}")