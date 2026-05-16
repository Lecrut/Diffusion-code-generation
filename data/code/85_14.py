from datetime import date
def weeks_difference(date1, date2):
    return (date2 - date1).days / 7
if __name__ == '__main__':
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 15)
    print(weeks_difference(d1, d2))