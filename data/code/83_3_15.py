from datetime import date

def are_dates_equal(d1, d2):
    return d1 == d2
if __name__ == '__main__':
    date_x = date(2023, 9, 15)
    date_y = date(2023, 9, 15)
    date_z = date(2023, 9, 16)
    result = are_dates_equal(date_x, date_y)
    print(result)
    result = are_dates_equal(date_x, date_z)
    print(result)