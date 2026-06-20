def calculate_month_difference(month1_name, month2_name):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if month1_name not in months or month2_name not in months:
        raise ValueError("Invalid month name provided.")
    month1 = months.index(month1_name) + 1
    month2 = months.index(month2_name) + 1
    return abs(month1 - month2)

if __name__ == '__main__':
    month_a = "December"
    month_b = "March"
    try:
        diff = calculate_month_difference(month_a, month_b)
        print(diff)
    except ValueError as e:
        print(e)