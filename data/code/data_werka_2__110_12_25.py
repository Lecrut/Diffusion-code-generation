def sort_date_tuples(dates):
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    def to_days(d):
        y, m, d_val = d
        total_days = y * 365 + (y // 4) - (y // 100) + (y // 400)
        for i in range(1, m):
            total_days += month_days[i]
        total_days += d_val
        return total_days

    return sorted(dates, key=to_days)

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