import datetime

def calculate_days(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        difference = abs(date1 - date2)
        return difference.days
    except ValueError:
        return "Error: Invalid date format. Please use YYYY-MM-DD."

if __name__ == '__main__':
    date1_input = "2023-04-01"
    date2_input = "2023-05-15"
    result = calculate_days(date1_input, date2_input)
    print(result)