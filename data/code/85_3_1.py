import datetime
def calculate_date_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        weeks = difference.days / 7
        return weeks
    except ValueError:
        return None
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2023-03-20"
    result = calculate_date_difference(date1_str, date2_str)
    if result is not None:
        print(f"Date 1: {date1_str}")
        print(f"Date 2: {date2_str}")
        print(f"Difference in weeks: {result:.2f}")
    else:
        print("Error: Invalid date format provided.")