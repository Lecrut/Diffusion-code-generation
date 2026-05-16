import datetime
def calculate_week_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        weeks = difference.days / 7
        print(f"Date 1: {date1.strftime('%Y-%m-%d')}")
        print(f"Date 2: {date2.strftime('%Y-%m-%d')}")
        print(f"Difference in weeks: {weeks:.2f}")
    except ValueError:
        print("Error: Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-03-20"
    calculate_week_difference(date1_input, date2_input)
    date1_input_invalid = "15/01/2023"
    date2_input_valid = "2023-03-20"
    calculate_week_difference(date1_input_invalid, date2_input_valid)