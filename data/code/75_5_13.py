import datetime

def calculate_date_difference(date1, date2):
    delta = abs(date2 - date1)
    return delta.days
if __name__ == '__main__':
    date_obj1 = datetime.date(2023, 9, 15)
    date_obj2 = datetime.date(2023, 9, 10)
    difference = calculate_date_difference(date_obj1, date_obj2)
    print(difference)