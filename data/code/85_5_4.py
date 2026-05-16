import datetime
def date_to_ordinal(date_str):
    year, month, day = map(int, date_str.split('-'))
    return datetime.date(year, month, day).toordinal()
def weeks_difference(date1_str, date2_str):
    ordinal1 = date_to_ordinal(date1_str)
    ordinal2 = date_to_ordinal(date2_str)
    difference = abs(ordinal1 - ordinal2)
    return difference // 7
if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-08"
    result = weeks_difference(date1, date2)
    print(result)