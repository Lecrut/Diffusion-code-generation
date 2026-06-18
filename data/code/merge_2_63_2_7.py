import datetime
class DateSubtractor:
    def subtract_years(self, date_input, year_count):
        try:
            parsed_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            result_date = parsed_date.replace(year=parsed_date.year - int(year_count))
            return f"{result_date.strftime('%Y-%m-%d')}"
        except ValueError as e:
            raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD'. Error details: {e}")
if __name__ == '__main__':
    subtractor = DateSubtractor()
    sample_dates = ["2023-10-05", "invalid-date"]
    test_years = [5, -2]
    for date_str in sample_dates:
        print(f"Input: {date_str}")
        try:
            result = subtractor.subtract_years(date_str, 5)
            print(f"Result (minus 5 years): {result}")
        except ValueError as ve:
            print(f"Error: {ve}")
        try:
            result_neg = subtractor.subtract_years(date_str, -2)
            print(f"Result (plus 2 years): {result_neg}")
        except ValueError as ve:
            print(f"Error with negative count: {ve}")