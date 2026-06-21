import datetime

def check_for_weekdays(date_strings):
    def is_valid_date_string(date_str):
        if not isinstance(date_str, str):
            return False
        try:
            datetime.datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def is_weekday(date_str):
        parsed_date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return parsed_date.weekday() < 5

    valid_dates = [d for d in date_strings if is_valid_date_string(d)]
    weekday_dates = [d for d in valid_dates if is_weekday(d)]
    
    return weekday_dates

if __name__ == '__main__':
    sample_dates = ["2023-10-01", "2023-10-02", "2023-10-07", "2023-10-08"]
    result = check_for_weekdays(sample_dates)
    print(result)