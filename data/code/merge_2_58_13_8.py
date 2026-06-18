import datetime
def calculate_date_difference(start_str: str, end_str: str) -> int:
    start = datetime.datetime.strptime(start_str, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_str, "%Y-%m-%d")
    delta = end - start
    return delta.days
if __name__ == '__main__':
    sample_start = "2023-10-05"
    sample_end = "2024-01-15"
    result_days = calculate_date_difference(sample_start, sample_end)
    print(f"Difference between {sample_start} and {sample_end}: {result_days} days")