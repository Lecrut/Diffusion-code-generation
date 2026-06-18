import datetime
def is_date_in_range(start_date_str: str, end_date_str: str, target_date_str: str) -> bool:
    try:
        start = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
        end = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        target = datetime.datetime.strptime(target_date_str, "%Y-%m-%d")
        return start <= target <= end
    except ValueError:
        raise ValueError("Invalid date format. Expected YYYY-MM-DD.")
if __name__ == '__main__':
    START_DATE = "2023-01-01"
    END_DATE = "2024-12-31"
    TARGET_DATE = "2023-06-15"
    result = is_date_in_range(START_DATE, END_DATE, TARGET_DATE)
    print(f"{TARGET_DATE} falls within the range [{START_DATE}, {END_DATE}]") if result else f"{TARGET_DATE} does not fall within the range [{START_DATE}, {END_DATE}]"