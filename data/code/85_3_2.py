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
    date1_input = "2023-01-15"
    date2_input = "2023-03-20"
    result = calculate_date_difference(date1_input, date2_input)
    print(result)