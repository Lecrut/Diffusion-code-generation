import datetime
def verify_date_in_range(date_str: str, start_str: str, end_str: str) -> bool:
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        start = datetime.datetime.strptime(start_str, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_str, "%Y-%m-%d")
        return start <= date <= end
    except ValueError as e:
        raise ValueError(f"Invalid date format. Expected 'YYYY-MM-DD'. Error: {e}")
if __name__ == '__main__':
    sample_date = "2023-10-15"
    sample_start = "2023-10-01"
    sample_end = "2023-10-31"
    result = verify_date_in_range(sample_date, sample_start, sample_end)
    print(result)