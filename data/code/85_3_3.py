import datetime
def calculate_date_difference(date_str1, date_str2):
    try:
        date1 = datetime.datetime.strptime(date_str1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date_str2, '%Y-%m-%d')
        difference = abs(date1 - date2)
        weeks = difference.days / 7
        return weeks
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."
if __name__ == '__main__':
    date1_str = "2023-01-01"
    date2_str = "2023-01-29"
    result = calculate_date_difference(date1_str, date2_str)
    print(result)