from datetime import date
class DateSubtractor:
    def subtract_years(self, current_date: date, years_to_subtract: int) -> date | None:
        try:
            if not isinstance(current_date, date):
                raise TypeError("Input must be a date object.")
            if not isinstance(years_to_subtract, int):
                raise ValueError("Years to subtract must be an integer.")
            new_year = current_date.year - years_to_subtract
            if new_year <= 0:
                return None
            try:
                result_date = date(new_year, current_date.month, current_date.day)
                if not (result_date.year == new_year and 
                        result_date.month == current_date.month and 
                        result_date.day == current_date.day):
                    raise ValueError(f"Invalid date: {current_date} minus {years_to_subtract} years results in an invalid calendar day.")
                return result_date
            except ValueError as e:
                if "invalid calendar day" not in str(e).lower():
                    raise
        except (TypeError, ValueError) as e:
            raise RuntimeError(f"Invalid input provided for date subtraction: {e}")
if __name__ == '__main__':
    subtractor = DateSubtractor()
    sample_date1 = date(2023, 5, 15)
    result1 = subtractor.subtract_years(sample_date1, 5)
    if result1:
        print(f"Result for {sample_date1} - 5 years: {result1}")
    else:
        print("No valid date found after subtraction.")
    try:
        bad_input = "not a date"
        result2 = subtractor.subtract_years(bad_input, 3)
    except RuntimeError as e:
        print(f"Caught expected error for invalid input type: {e}")
    sample_date2 = date(2024, 1, 31)
    result2 = subtractor.subtract_years(sample_date2, 5)
    print(f"Result for {sample_date2} - 5 years: {result2}")