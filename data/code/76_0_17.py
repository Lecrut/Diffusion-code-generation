import datetime

def calculate_days(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d').date()
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d').date()
        difference = abs((date2 - date1).days)
        return difference
    except ValueError:
        raise ValueError("Error: Invalid date format. Please use YYYY-MM-DD.")

if __name__ == '__main__':
    date1_input = "2023-01-15"
    date2_input = "2023-03-20"
    result = calculate_days(date1_input, date2_input)
    print(result)