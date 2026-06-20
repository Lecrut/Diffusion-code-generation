def month_difference(months, start_month, end_month):
    month_map = {month: i for i, month in enumerate(months)}
    start_index = month_map[start_month]
    end_index = month_map[end_month]
    return abs(end_index - start_index)

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(month_difference(months, "January", "July"))