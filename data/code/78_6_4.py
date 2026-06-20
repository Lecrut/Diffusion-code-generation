import calendar

def months_difference(date1, date2):
    year1, month1, _ = map(int, date1.split('-'))
    year2, month2, _ = map(int, date2.split('-'))
    return (year2 - year1) * 12 + (month2 - month1)
if __name__ == '__main__':
    print(months_difference('2023-04-01', '2022-05-01'))