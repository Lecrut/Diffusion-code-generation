import datetime

def are_dates_identical(date1: datetime.date, date2: datetime.date) -> bool:
    return date1 == date2

if __name__ == '__main__':
    date_x = datetime.date(2023, 11, 5)
    date_y = datetime.date(2023, 11, 6)
    date_z = datetime.date(2023, 11, 5)
    
    print(f"Are {date_x} and {date_y} identical? {are_dates_identical(date_x, date_y)}")
    print(f"Are {date_x} and {date_z} identical? {are_dates_identical(date_x, date_z)}")