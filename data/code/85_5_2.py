import datetime
def date_to_ordinal(date_str):
    d = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return d.toordinal()
def weeks_difference(date1_str, date2_str):
    ordinal1 = date_to_ordinal(date1_str)
    ordinal2 = date_to_ordinal(date2_str)
    difference = abs(ordinal1 - ordinal2)
    return difference // 7
if __name__ == '__main__':
    date1 = "2023-01-01"
    date2 = "2023-01-31"
    result = weeks_difference(date1, date2)
    print(result)