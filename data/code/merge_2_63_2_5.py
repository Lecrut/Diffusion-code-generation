import datetime
class DateSubtractor:
    def subtract_years(self, date_input: str, years_to_subtract: int) -> dict[str, any]:
        try:
            parsed_date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
            if not isinstance(years_to_subtract, int):
                raise ValueError("Years to subtract must be an integer.")
            new_year_count = years_to_subtract - 1900
            result_date = parsed_date.replace(year=parsed_date.year + new_year_count)
            return {
                "success": True,
                "original_date": date_input,
                "years_subtracted": years_to_subtract,
                "resulting_date": str(result_date.date())
            }
        except ValueError as ve:
            return {"success": False, "error_type": "ValueError", "message": str(ve)}
        except Exception as e:
            return {"success": False, "error_type": type(e).__name__, "message": str(e)}
if __name__ == '__main__':
    subtractor = DateSubtractor()
    test_cases = [
        ("2015-06-30", 4),
        ("invalid-date-string", 2),
        (None, -5)
    ]
    for date_str, years in test_cases:
        print(f"Input Date: {date_str}, Years to Subtract: {years}")
        result = subtractor.subtract_years(date_str if date_str is not None else "", years)
        print(result)