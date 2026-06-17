class DateSubtractor:
    def subtract_years(self, date_str: str, years_to_subtract: int) -> tuple[int, int]:
        try:
            year = int(years_to_subtract)
            if year < 0:
                raise ValueError("Years to subtract must be non-negative.")
            current_year = int(date_str.split("-")[0])
            new_year = current_year - year
            return (new_year, date_str[-4:])
        except Exception as e:
            raise TypeError(f"Invalid input format or value. Error: {str(e)}")
if __name__ == '__main__':
    subtractor = DateSubtractor()
    test_cases = [
        ("2023-10-05", 5),
        ("2024-06-18", 2),
        ("2020-01-01", 1)
    ]
    for date_str, years in test_cases:
        try:
            result = subtractor.subtract_years(date_str, years)
            print(f"Input Date: {date_str}, Subtracting {years} Years -> New Year: {result[0]}")
        except Exception as e:
            print(f"Error processing input '{date_str}' with value {years}: {e}")