from datetime import datetime
def are_dates_identical(date1: datetime, date2: datetime) -> bool:
    return date1.date() == date2.date()
if __name__ == '__main__':
    date_a = datetime(2023, 10, 26, 14, 30)
    date_b = datetime(2023, 10, 26, 9, 0)
    date_c = datetime(2023, 11, 26, 10, 0)
    date_d = datetime(2022, 10, 26, 10, 0)
    print(f"Date A and Date B are identical: {are_dates_identical(date_a, date_b)}")
    print(f"Date A and Date C are identical: {are_dates_identical(date_a, date_c)}")
    print(f"Date A and Date D are identical: {are_dates_identical(date_a, date_d)}")
    print(f"Date B and Date C are identical: {are_dates_identical(date_b, date_c)}")
    print(f"Date C and Date D are identical: {are_dates_identical(date_c, date_d)}")