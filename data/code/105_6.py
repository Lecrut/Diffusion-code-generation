import datetime
def nth_day_after(start_date, n):
    date_format = "%Y-%m-%d"
    try:
        start = datetime.datetime.strptime(start_date, date_format)
        if n < 0:
            raise ValueError("N must be non-negative")
        result = start + datetime.timedelta(days=n)
        return result.strftime(date_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format or input: {e}")
if __name__ == '__main__':
    start_date_str = "2023-10-26"
    n_value = 10
    try:
        result_date = nth_day_after(start_date_str, n_value)
        print(result_date)
    except ValueError as e:
        print(f"Error: {e}")