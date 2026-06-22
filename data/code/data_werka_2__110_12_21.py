def sort_date_tuples(dates):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def date_to_days(date_tuple):
        year, month, day = date_tuple
        total_days = 0
        for y in range(1, year):
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                total_days += 366
            else:
                total_days += 365
        for m in range(1, month):
            days_in_m = month_days[m]
            if m == 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                days_in_m += 1
            total_days += days_in_m
        total_days += day
        return total_days

    return sorted(dates, key=date_to_days)

if __name__ == '__main__':
    sample_dates = [
        (2023, 10, 15),
        (1999, 1, 1),
        (2023, 1, 1),
        (2023, 10, 1),
        (1999, 12, 31)
    ]
    sorted_dates = sort_date_tuples(sample_dates)
    print(sorted_dates)