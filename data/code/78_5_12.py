def month_difference(months, start_month, end_month):
    start_index = months.index(start_month)
    end_index = months.index(end_month)
    diff = abs(end_index - start_index)
    return min(diff, len(months) - diff)

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = month_difference(months, "January", "July")
    print(result)