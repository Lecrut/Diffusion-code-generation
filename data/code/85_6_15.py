DAYS_PER_WEEK = 7

def calculate_week_difference(date1, date2):
    diff = abs((date1 - date2).days)
    return diff // DAYS_PER_WEEK

if __name__ == '__main__':
    date1 = '2023-01-01'
    date2 = '2023-01-15'
    print(calculate_week_difference(date1, date2))