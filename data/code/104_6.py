from datetime import datetime
def date_difference_days(date_str1, date_str2):
    date1 = datetime.strptime(date_str1, '%Y-%m-%d')
    date2 = datetime.strptime(date_str2, '%Y-%m-%d')
    if date1 > date2:
        return (date1 - date2).days
    else:
        return (date2 - date1).days
if __name__ == '__main__':
    date_a = "2023-01-15"
    date_b = "2023-03-01"
    difference1 = date_difference_days(date_a, date_b)
    print(difference1)