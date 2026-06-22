from datetime import date

class DateValidator:
    def validate_date(self, date_str):
        try:
            return date.fromisoformat(date_str)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}")

    def is_weekend(self, date_obj):
        weekday = date_obj.weekday()
        return weekday >= 5

if __name__ == '__main__':
    validator = DateValidator()
    
    dates_to_check = ['2023-10-06', '2023-10-07', '2023-10-08']
    results = {date_str: validator.is_weekend(validator.validate_date(date_str)) for date_str in dates_to_check}
    
    for date_str, is_weekend in results.items():
        print(f"Is {date_str} a weekend? {is_weekend}")