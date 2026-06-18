import datetime
def is_date_in_range(date_str: str, start_str: str, end_str: str) -> bool:
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        start = datetime.datetime.strptime(start_str, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_str, "%Y-%m-%d")
        return start <= date <= end
    except ValueError:
        return False
if __name__ == '__main__':
    sample_date = "2023-10-15"
    range_start = "2023-10-01"
    range_end = "2023-10-31"
    result = is_date_in_range(sample_date, range_start, range_end)
    print(result)