def month_difference(months, start_month, end_month):
    month_map = {month: i for i, month in enumerate(months)}
    start_index = month_map[start_month]
    end_index = month_map[end_month]
    diff = abs(end_index - start_index)
    return min(diff, 12 - diff)

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = month_difference(months, "March", "October")
    print(result)