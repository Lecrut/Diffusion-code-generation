def validate_month_name(month_name):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if month_name not in months:
        raise ValueError("Invalid month name provided")

def get_month_index(months, month_name):
    return months.index(month_name)

def month_difference(months, start_month, end_month):
    validate_month_name(start_month)
    validate_month_name(end_month)
    start_index = get_month_index(months, start_month)
    end_index = get_month_index(months, end_month)
    return abs(end_index - start_index)

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = month_difference(months, "January", "July")
    print(result)