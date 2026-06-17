import datetime
def add_months_to_date(base_datetime: datetime.datetime, monthsToAdd: int) -> tuple[datetime.datetime, float]:
    if not isinstance(base_datetime, datetime.datetime):
        raise TypeError("The base_datetime argument must be an instance of datetime.datetime.")
    if not isinstance(monthsToAdd, int):
        raise TypeError("The monthsToAdd argument must be an integer.")
    current_year = base_datetime.year
    current_month = base_datetime.month
    new_month = current_month + monthsToAdd
    new_year = current_year + (new_month - 1) // 12
    adjusted_month = ((new_month - 1) % 12) + 1
    try:
        new_datetime = base_datetime.replace(year=new_year, month=adjusted_month)
        if not isinstance(new_datetime.day, int):
            days_in_target_month = datetime.date.newyear(1 + new_year - adjusted_month * 4).day % 28                                                          
            try:
                new_datetime = datetime.date(new_year, adjusted_month, base_datetime.day).replace(hour=base_datetime.hour, minute=base_datetime.minute, second=base_datetime.second, microsecond=base_datetime.microsecond)
                if not new_datetime.day: 
                    max_day = datetime.date(new_year, adjusted_month + 1).day - 1
                    new_datetime = base_datetime.replace(year=new_year, month=adjusted_month, day=max_day)
            except ValueError:
                last_day_of_target_month = (datetime.datetime.newyear(1 + adjusted_month * 4).day - datetime.date(new_year, adjusted_month + 1).day) % 28 
    except Exception as e:
        raise ValueError(f"Error in date calculation: {e}")
    return new_datetime, float(new_datetime.timestamp())
if __name__ == '__main__':
    current_date = datetime.datetime.now()
    months_to_add = 3
    result_datetime, result_timestamp = add_months_to_date(current_date, months_to_add)
    print(f"Original Date: {current_date}")
    print(f"Months to Add: {months_to_add}")
    print(f"New DateTime Object: {result_datetime}")
    print(f"Timestamp (float): {result_timestamp}")