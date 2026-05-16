import datetime
def date_to_ordinal(date):
    return date.toordinal()
def weeks_difference(date1, date2):
    return (date_to_ordinal(date1) - date_to_ordinal(date2)) // 7
if __name__ == '__main__':
    date_a = datetime.date(2023, 1, 1)
    date_b = datetime.date(2023, 1, 8)
    difference = weeks_difference(date_a, date_b)
    print(difference)