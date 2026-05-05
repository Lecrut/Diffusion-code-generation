import datetime
def calculate_days_difference(date1_str, date2_str):
    try:
        date1 = datetime.datetime.strptime(date1_str, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2_str, '%Y-%m-%d')
        if date1 == date2:
            return 0
        if date1 < date2:
            difference = date2 - date1
        else:
            difference = date1 - date2
        return difference.days
    except ValueError as e:
        return f"Error parsing date: {e}"
    except TypeError:
        return "Error: Invalid input type provided."
if __name__ == '__main__':
    date1_str = "2023-01-15"
    date2_str = "2024-05-20"
    result = calculate_days_difference(date1_str, date2_str)
    if isinstance(result, int):
        print(result)
    else:
        print(result)