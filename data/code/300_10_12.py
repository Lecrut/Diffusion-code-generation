from datetime import date

def days_remaining_in_month(year, month):
    if 1 <= month <= 12:
        _, last_day = date(year, month, 1).monthrange()
        return last_day - date.today().day + 1
    else:
        raise ValueError("Month must be between 1 and 12")

if __name__ == '__main__':
    print(days_remaining_in_month(2023, 4))