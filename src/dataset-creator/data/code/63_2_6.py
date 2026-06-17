class DateSubtractor:
    def subtract_years(self, date_str: str, years_to_subtract: int) -> dict:
        import datetime
        try:
            if not isinstance(date_str, str):
                raise ValueError("Input date must be a string.")
            parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            if not isinstance(years_to_subtract, int) or years_to_subtract < 0:
                raise TypeError("Years to subtract must be a non-negative integer.")
            new_year_count = parsed_date.year - years_to_subtract
            try:
                result_date = datetime.datetime(new_year_count, parsed_date.month, parsed_date.day).date()
            except ValueError as e:
                return {"success": False, "error_message": f"Invalid date components after subtraction: {str(e)}"}
            return {
                "success": True,
                "original_date": date_str,
                "years_subtracted": years_to_subtract,
                "resulting_date": result_date.isoformat()
            }
        except ValueError as e:
            return {"success": False, "error_message": f"Invalid input format or value: {str(e)}"}
if __name__ == '__main__':
    sample_dates = ["2023-10-05", "invalid-date"]
    subtract_years_values = [1, 2]
    for date_str in sample_dates:
        for years_to_subtract in subtract_years_values:
            result = DateSubtractor().subtract_years(date_str, years_to_subtract)
            print(result)