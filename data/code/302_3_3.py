def days_in_month(year):
    import calendar
    return {month: calendar.monthrange(year, month)[1] for month in range(1, 13)}

if __name__ == '__main__':
    print(days_in_month(2023))