from datetime import date

def week_difference(date1: date, date2: date) -> int:
    if date1 > date2:
        date1, date2 = (date2, date1)
    return (date2 - date1).days // 7
if __name__ == '__main__':
    print(week_difference(date(2023, 1, 1), date(2023, 1, 8)))
    print(week_difference(date(2023, 1, 8), date(2023, 1, 1)))
    print(week_difference(date(2023, 1, 1), date(2023, 2, 1)))
    print(week_difference(date(2023, 2, 1), date(2023, 1, 1)))