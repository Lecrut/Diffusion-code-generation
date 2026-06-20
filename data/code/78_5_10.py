def validate_months(months, month1, month2):
    if month1 not in months or month2 not in months:
        raise ValueError("Invalid month name provided")

def calculate_month_difference(months, start_month, end_month):
    start_index = months.index(start_month)
    end_index = months.index(end_month)
    return abs(end_index - start_index)

def month_difference(months, start_month, end_month):
    validate_months(months, start_month, end_month)
    return calculate_month_difference(months, start_month, end_month)

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(month_difference(months, "January", "July"))