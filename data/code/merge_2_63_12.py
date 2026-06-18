from datetime import date
def calculate_future_date(iso_string: str, year_diff: int) -> str:
    try:
        current_date = date.fromisoformat(iso_string)
        new_year = current_date.year + year_diff
        return f"{new_year}-{current_date.month:02d}-{current_date.day:02d}"
    except ValueError as e:
        raise ValueError(f"Invalid ISO format or unsupported operation: {e}")
if __name__ == '__main__':
    sample_input = "2023-10-05"
    diff_value = 5
    result_date = calculate_future_date(sample_input, diff_value)
    print(result_date)