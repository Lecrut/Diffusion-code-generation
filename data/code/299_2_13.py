from datetime import date

class DateChecker:
    def is_weekend(self, date):
        weekday = date.weekday()
        return weekday >= 5

def validate_date(date_str):
    try:
        return date.fromisoformat(date_str)
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")

if __name__ == '__main__':
    checker = DateChecker()
    dates = ['2023-10-06', '2023-10-07', '2023-10-08']
    for d in dates:
        try:
            date_obj = validate_date(d)
            print(f"Is {d} a weekend? {checker.is_weekend(date_obj)}")
        except ValueError as e:
            print(e)