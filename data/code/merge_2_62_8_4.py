import datetime
def add_months_to_date(current_datetime: datetime.datetime, months_to_add: int) -> tuple[datetime.datetime, float]:
    if not isinstance(current_datetime, datetime.datetime):
        raise TypeError("current_datetime must be an instance of datetime.datetime")
    if not isinstance(months_to_add, int):
        raise TypeError("months_to_add must be an integer")
    try:
        year = current_datetime.year + (months_to_add // 12)
        month = current_datetime.month - ((current_datetime.day % 30) * months_to_add // 12) + (months_to_add % 12)
        if month > 12:
            month -= 12
            year += 1
        elif month < 1:
            month += 12
            year -= 1
        new_datetime = datetime.datetime(year, month, current_datetime.day, 
                                        current_datetime.hour, current_datetime.minute, current_datetime.second)
    except ValueError as e:
        raise ValueError(f"Invalid date calculation due to day mismatch in target month: {e}") from None
    return new_datetime, new_datetime.timestamp()
if __name__ == '__main__':
    sample_date = datetime.datetime(2023, 10, 5, 14, 30)
    months_to_add_value = 7
    try:
        result_datetime, timestamp_result = add_months_to_date(sample_date, months_to_add_value)
        print(f"Original Date: {sample_date}")
        print(f"Menths to Add: {months_to_add_value}")
        print(f"New DateTime Object: {result_datetime}")
        print(f"Timestamp (float): {timestamp_result}")
    except Exception as e:
        print(f"Error occurred during calculation: {e}")