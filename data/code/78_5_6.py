MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def month_index(month):
    return MONTHS.index(month)

def month_difference(months, start_month, end_month):
    start_idx = month_index(start_month)
    end_idx = month_index(end_month)
    return abs(end_idx - start_idx)

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(month_difference(months, "January", "July"))