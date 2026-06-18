from datetime import date
class DateSubtractor:
    def subtract_years(self, start_date: date, years_to_subtract: int) -> date | None:
        try:
            if not isinstance(start_date, date):
                raise TypeError("start_date must be of type 'datetime.date'")
            if not isinstance(years_to_subtract, int) or isinstance(years_to_subtract, bool):
                raise TypeError("years_to_subtract must be an integer")
            if years_to_subtract < 0:
                raise ValueError("years_to_subtract cannot be negative")
            new_year = start_date.year - years_to_subtract
            try:
                return date(new_year, start_date.month, start_date.day)
            except ValueError:
                raise
        except TypeError as te:
            print(f"Input Error: {te}")
            return None
        except ValueError as ve:
            print(f"Value Error: {ve}")
            return None
if __name__ == '__main__':
    test_cases = [
        (date(2023, 12, 31), -5),                                        
        (date(2024, 2, 29), -1),                                                                                                                                                                                                                                                                           
        (date(2023, 4, 15), -1),                                                                              
        ("invalid_date", -1),                                
        (date(2023, 6, 30), -1),                                                           
    ]
    processor = DateSubtractor()
    print("Running DateSubtractor tests...\n")
    for i, args in enumerate(test_cases):
        if len(args) == 2:
            d_input, y_subtract = args
            result_date = None
            error_msg = ""
            try:
                result_date = processor.subtract_years(d_input, y_subtract)
            except Exception as e:
                error_msg = str(e)
            print(f"Test Case {i+1}:")
            print(f"  Input Date: {d_input}")
            print(f"  Years to Subtract: {y_subtract}")
            if result_date is not None and "None" in str(result_date):                                                                                     
                pass
            print(f"  Result: {result_date}")
            if result_date is not None and "None" in str(result_date):
                 print("  Status: Error occurred (returned None)")
            else:
                 print("  Status: Success")
    try:
        bad_result = processor.subtract_years(12345, -1)
        if bad_result is not None and "None" in str(bad_result):
            pass 
    except Exception as e:
        print(f"Unexpected exception during test run: {e}")