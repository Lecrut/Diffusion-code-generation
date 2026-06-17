def add_years(date_str: str, years: int) -> str:
    try:
        from datetime import datetime
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        new_dt = dt.replace(year=dt.year + years)
        return new_dt.strftime("%Y-%m-%d")
    except ValueError as e:
        raise RuntimeError(f"Invalid date format. Expected YYYY-MM-DD.") from e
if __name__ == '__main__':
    result = add_years("2023-10-05", 2)
    print(result)