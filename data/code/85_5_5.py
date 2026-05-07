import datetime
def date_to_ordinal(date):
    return date.toordinal()
def weeks_difference(date1, date2):
    ord1 = date_to_ordinal(date1)
    ord2 = date_to_ordinal(date2)
    difference = abs(ord1 - ord2)
    return difference // 7
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 8)
    result = weeks_difference(date_a, date_b)
    print(result)