MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
INDEX_MAP = {month: idx for idx, month in enumerate(MONTHS)}

def month_difference(months, start_month, end_month):
    start_index = INDEX_MAP[start_month]
    end_index = INDEX_MAP[end_month]
    return abs(end_index - start_index)

if __name__ == '__main__':
    months = MONTHS
    print(month_difference(months, "January", "July"))