import datetime

def compare_dates(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d').date()
        return min(date1, date2)
    except ValueError:
        raise ValueError("Error: One or both date strings are in an invalid format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1_input = "2023-10-25"
    date2_input = "2023-10-15"
    try:
        earlier_date = compare_dates(date1_input, date2_input)
        print(f"The earlier date is: {earlier_date}")
    except ValueError as e:
        print(e)