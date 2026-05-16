import datetime
def date_to_ordinal(date_str):
    year, month, day = map(int, date_str.split('-'))
    return datetime.date(year, month, day).toordinal()
def weeks_difference(date1_str, date2_str):
    ordinal1 = date_to_ordinal(date1_str)
    ordinal2 = date_to_ordinal(date2_str)
    difference_days = abs(ordinal1 - ordinal2)
    return difference_days / 7.0
if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-01-08"
    result = weeks_difference(date_a, date_b)
    print(result)