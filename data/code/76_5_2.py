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
    date1_str = '10/20/2023'
    date2_str = '11/15/2023'
    print(f"Difference between {date1_str} and {date2_str}: {calculate_date_difference(date1_str, date2_str)} days")
    date3_str = '01/01/2024'
    date4_str = '01/01/2024'
    print(f"Difference between {date3_str} and {date4_str}: {calculate_date_difference(date3_str, date4_str)} days")
    date5_str = '12/31/2022'
    date6_str = '01/01/2023'
    print(f"Difference between {date5_str} and {date6_str}: {calculate_date_difference(date5_str, date6_str)} days")
    try:
        calculate_date_difference('2023-10-20', '2023-11-15')
    except ValueError as e:
        print(f"Error caught for invalid format: {e}")
    try:
        calculate_date_difference('10-20-2023', '11-15-2023')
    except ValueError as e:
        print(f"Error caught for invalid format: {e}")