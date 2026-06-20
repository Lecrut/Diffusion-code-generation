def weeks_between_dates(date1, date2):
    days_in_week = 7
    return abs((date2 - date1) // days_in_week)
if __name__ == '__main__':
    print(weeks_between_dates(20230401, 20230501))