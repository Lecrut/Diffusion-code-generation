def month_difference(months, start_month, end_month):
    if start_month not in months or end_month not in months:
        raise ValueError("Invalid month name provided")
    
    start_index = months.index(start_month)
    end_index = months.index(end_month)
    
    return min(abs(end_index - start_index), 12 - abs(end_index - start_index))

if __name__ == '__main__':
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    result = month_difference(months, "January", "July")
    print(result)