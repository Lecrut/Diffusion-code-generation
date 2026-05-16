import datetime
def get_day_of_month(date_string: str) -> int:
    try:
        date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        return date_object.day
    except ValueError:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD.")
if __name__ == '__main__':
    sample_date_1 = "2023-10-27"
    sample_date_2 = "1999-01-01"
    sample_date_3 = "2024-02-29"
    print(f"Date: {sample_date_1}, Day: {get_day_of_month(sample_date_1)}")
    print(f"Date: {sample_date_2}, Day: {get_day_of_month(sample_date_2)}")
    print(f"Date: {sample_date_3}, Day: {get_day_of_month(sample_date_3)}")