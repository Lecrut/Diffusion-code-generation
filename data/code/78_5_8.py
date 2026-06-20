months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def month_index(month_name):
    return months.index(month_name)

def month_difference(months, start_month, end_month):
    start_idx = month_index(start_month)
    end_idx = month_index(end_month)
    diff = abs(end_idx - start_idx)
    return min(diff, 12 - diff)

if __name__ == '__main__':
    result = month_difference(months, "January", "July")
    print(result)