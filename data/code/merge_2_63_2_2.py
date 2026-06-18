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
            print(f"[ERROR] Type Error: {te}")
            return None
if __name__ == '__main__':
    test_cases = [
        (date(2023, 12, 31), 5),                                                                                   
        (date(2024, 2, 29), 1),                                   
        ("invalid_date", -1),                                       
        (date(2023, 6, 15), "years"),                                          
    ]
    subtractor = DateSubtractor()
    print("Running production tests...\n")
    for i, args in enumerate(test_cases):
        try:
            if len(args) == 2:
                d_input, y_input = args
                result = subtractor.subtract_years(d_input, y_input)
                print(f"Test Case {i+1}:")
                print(f"Input Date: {d_input}")
                print(f"Years to Subtract: {y_input}")
                if isinstance(result, date):
                    print(f"Result: {result}\n")
                else:
                    print("Error occurred during processing.\n")
            else:
                print(f"Test Case {i+1}: Skipped due to argument mismatch\n")
        except Exception as e:
            error_msg = f"[ERROR] Unexpected exception in Test Case {i+1}: {type(e).__name__} - {e}"
            print(error_msg + "\n")
    print("All tests completed.")