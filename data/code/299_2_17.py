from datetime import date

def is_valid_date(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False

class DateChecker:
    def is_weekend(self, date_obj):
        weekday = date_obj.weekday()
        return weekday >= 5

if __name__ == '__main__':
    checker = DateChecker()
    dates = ['2023-10-06', '2023-10-07', '2023-10-08']
    
    for date_str in dates:
        if is_valid_date(date_str):
            date_obj = date.fromisoformat(date_str)
            print(f"Is {date_str} a weekend? {checker.is_weekend(date_obj)}")
        else:
            print(f"{date_str} is not a valid date.")