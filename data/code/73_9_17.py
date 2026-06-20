from datetime import datetime

def calculate_time_difference(date1, date2):
    return abs(date1 - date2)

if __name__ == '__main__':
    sample_dates = [
        ("2023-01-15", "2023-02-20"),
        ("2022-11-20", "2023-12-31"),
        ("2023/01/10", "2023-01-15")
    ]
    
    for date_str1, date_str2 in sample_dates:
        try:
            date1 = datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.strptime(date_str2, '%Y-%m-%d')
            difference = calculate_time_difference(date1, date2)
            print(f"Date 1: {date_str1}, Date 2: {date_str2}, Time Difference: {difference}")
        except ValueError:
            print(f"Error: Invalid date format. Please use YYYY-MM-DD for {date_str1} or {date_str2}.")