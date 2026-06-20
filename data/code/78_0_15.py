def calculate_month_difference(month1_name, month2_name):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if month1_name not in months or month2_name not in months:
        raise ValueError("Invalid month name provided.")
    month1_index = months.index(month1_name)
    month2_index = months.index(month2_name)
    difference = abs(month1_index - month2_index)
    return difference

if __name__ == '__main__':
    month_a = "December"
    month_b = "March"
    try:
        result = calculate_month_difference(month_a, month_b)
        print(result)
    except ValueError as e:
        print(e)