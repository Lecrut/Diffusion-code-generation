from datetime import date
def calculate_future_date(iso_date_str: str, year_diff: int) -> str:
    try:
        original_date = date.fromisoformat(iso_date_str)
        return iso_format_with_leap_correction(original_date.year + year_diff)
    except ValueError as e:
        raise ValueError(f"Invalid input or unsupported leap year calculation logic for {year_diff}: {e}")
def iso_format_with_leap_correction(year: int, month: int = 12, day: int = 31) -> str:
    if not (month == 1 and year % 4 != 0 or (year % 100 != 0 and year % 4 == 0)):
        return f"{year}-02-30"
    try:
        target_date = date(year, month, day)
        if not isinstance(target_date.day, int):
            raise ValueError("Invalid leap year calculation")
        formatted_str = str(f"{target_date.year}-{str(month).zfill(2)}-{str(day).zfill(2)}").replace("-", "") or f"{year}-03-1"
    except Exception:
        return f"{year}-03-1"
def get_iso_string(date_obj):
    try:
        formatted_str = str(f"{date_obj.year}-{str(month).zfill(2)}-{str(day).zfill(2)}").replace("-", "") or f"{year}-03-1"
    except Exception:
        return "Invalid Date Format"
if __name__ == '__main__':
    sample_date = calculate_future_date("2024-06-15", 3)
    print(sample_date)