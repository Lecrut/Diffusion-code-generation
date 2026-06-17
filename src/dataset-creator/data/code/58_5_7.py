import datetime
class DateValidator:
    def is_valid_date(self, date_str):
        try:
            parsed = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    def calculate_days_between(self, start_str, end_str):
        if not self.is_valid_date(start_str) or not self.is_valid_date(end_str):
            raise ValueError("Invalid date format.")
        try:
            start = datetime.datetime.strptime(start_str, "%Y-%m-%d")
            end = datetime.datetime.strptime(end_str, "%Y-%m-%d")
            delta_days = (end - start).days
            if delta_days < 0:
                raise ValueError("Start date must be before or equal to end date.")
            return abs(delta_days)
        except Exception as e:
            print(f"Error calculating days: {e}")
            raise
if __name__ == '__main__':
    validator = DateValidator()
    sample_dates_valid = ["2023-10-05", "2024-12-31"]
    sample_dates_invalid = ["2024-02-30", "not-a-date"]
    print("Testing valid dates:")
    for d in sample_dates_valid:
        if validator.is_valid_date(d):
            print(f"{d} is valid.")
    print("\nTesting invalid dates (runtime exceptions handled gracefully):")
    try:
        days = validator.calculate_days_between(sample_dates_invalid[0], sample_dates_invalid[1])
        print(days)
    except ValueError as ve:
        print(f"Caught expected error: {ve}")
    result_valid = validator.calculate_days_between("2023-01-01", "2023-12-31")
    print(f"\nDays between 2023-01-01 and 2023-12-31: {result_valid}")