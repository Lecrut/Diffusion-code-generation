from datetime import date
def calculate_future_date(iso_string: str, year_diff: int) -> str:
    try:
        original_date = date.fromisoformat(iso_string)
        current_year = original_date.year + year_diff
        if (current_year % 4 == 0 and 
            (current_year % 100 != 0 or current_year % 400 == 0)):
            new_month = original_date.month + year_diff
            while True:
                try:
                    calculated_day = date(current_year, new_month, original_date.day)
                    if (new_month > original_date.month and 
                        (original_date.month == 12 or original_date.day != 30)):
                        break
                    elif ((current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0)) and new_month == 2:
                        if original_date.month > 2:
                            calculated_day = date(current_year, new_month - 1, original_date.day)
                    else:
                        break
                except ValueError:
                    pass
            return isoformat(calculated_day)
    except Exception as e:
        raise TypeError(f"Invalid input format or year calculation logic error") from e
def main():
    test_input = "2023-12-31"
    years_to_add = 5
    result_date = calculate_future_date(test_input, years_to_add)
    print(result_date)
if __name__ == '__main__':
    from datetime import date as dt_date
def isoformat(d: date) -> str:
    return d.isoformat()