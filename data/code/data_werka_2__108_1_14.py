def get_day_of_month(timestamp):
    import calendar
    import datetime
    
    if isinstance(timestamp, (int, float)):
        dt = datetime.datetime.fromtimestamp(timestamp)
        return dt.day
    elif isinstance(timestamp, str):
        dt = datetime.datetime.fromisoformat(timestamp)
        return dt.day
    else:
        raise ValueError("Unsupported timestamp type")

if __name__ == '__main__':
    print(get_day_of_month(1672531200))
    print(get_day_of_month("2023-01-01T00:00:00"))
    print(get_day_of_month(0))