import datetime
def is_date_in_range(target_date_str: str, start_date_str: str, end_date_str: str) -> bool:
    try:
        target = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
        start = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        return start <= target <= end
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
if __name__ == '__main__':
    sample_target = "2023-12-25"
    sample_start = "2023-12-01"
    sample_end = "2024-01-01"
    result = is_date_in_range(sample_target, sample_start, sample_end)
    print(result)