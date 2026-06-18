from datetime import date
class DateSubtractor:
    def subtract_years(self, start_date: date, years_to_subtract: int) -> date | None:
        try:
            if not isinstance(start_date, date):
                raise TypeError("start_date must be of type 'datetime.date'")
            if not isinstance(years_to_subtract, int) or years_to_subtract < 0:
                raise ValueError(f"years_to_subtract must be a non-negative integer. Got {type(years_to_subtract).__name__}")
            new_year = start_date.year - years_to_subtract
            try:
                return date(new_year, start_date.month, start_date.day)
            except ValueError as e:
                raise ValueError(f"Invalid calendar combination after subtraction. Original: {start_date}, New Year: {new_year}") from e
        except TypeError as te:
            raise type(te)(f"{te.message} for input types.") from te
if __name__ == '__main__':
    original_date = date(2023, 12, 31)
    try:
        result = DateSubtractor().subtract_years(original_date, 5)
        print(f"Original Date: {original_date}")
        print(f"Date after subtracting 5 years: {result}")
        bad_input_1 = "2023-12-31"
        try:
            result_bad = DateSubtractor().subtract_years(bad_input_1, 5)
        except TypeError as e:
            print(f"\nCaught expected error for string input: {e}")
    except Exception as ex:
        print(f"Unexpected Error occurred: {ex}")