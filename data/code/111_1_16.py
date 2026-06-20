import datetime

class DateModifier:
    def add_days_to_date(self, date_obj, days):
        return date_obj + datetime.timedelta(days=days)

if __name__ == '__main__':
    modifier = DateModifier()
    original_date = datetime.date(2024, 7, 4)
    new_date = modifier.add_days_to_date(original_date, 30)
    print(f"Original: {original_date}, New: {new_date}")