import datetime

def date_to_ordinal(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").toordinal()

def weeks_difference(date1_str, date2_str):
    ordinal1 = date_to_ordinal(date1_str)
    ordinal2 = date_to_ordinal(date2_str)
    difference = abs(ordinal1 - ordinal2)
    return difference // 7

if __name__ == '__main__':
    date_a = "2023-01-01"
    date_b = "2023-02-15"
    result = weeks_difference(date_a, date_b)
    print(result)