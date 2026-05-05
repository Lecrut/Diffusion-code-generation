import datetime
def days_elapsed(date1, date2):
    if date1 < date2:
        return (date2 - date1).days
    else:
        return (date1 - date2).days
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 10)
    result1 = days_elapsed(date_a, date_b)
    print(result1)
    date_c = datetime.date(2024, 5, 15)
    date_d = datetime.date(2024, 4, 1)
    result2 = days_elapsed(date_c, date_d)
    print(result2)