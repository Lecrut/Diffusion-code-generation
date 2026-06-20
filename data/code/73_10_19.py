from datetime import datetime

def calculate_time_difference(date_str1, date_str2):
    try:
        dt1 = datetime.strptime(date_str1, '%Y-%m-%d')
        dt2 = datetime.strptime(date_str2, '%Y-%m-%d')
        return abs((dt2 - dt1).days)
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-05"
    difference = calculate_time_difference(date1, date2)
    print(f"Days between {date1} and {date2}: {difference}")

    date3 = "2024-06-15"
    date4 = "2024-06-15"
    difference2 = calculate_time_difference(date3, date4)
    print(f"Days between {date3} and {date4}: {difference2}")

    date5 = "2023-12-31"
    date6 = "2024-01-01"
    difference3 = calculate_time_difference(date5, date6)
    print(f"Days between {date5} and {date6}: {difference3}")