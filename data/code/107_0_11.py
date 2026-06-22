from datetime import datetime

_MONTH_PAD = {
    1: '01', 2: '02', 3: '03', 4: '04',
    5: '05', 6: '06', 7: '07', 8: '08',
    9: '09', 10: '10', 11: '11', 12: '12'
}

_DAY_PAD = {
    i: f'{i:02d}' for i in range(1, 32)
}

_HOUR_PAD = {
    i: f'{i:02d}' for i in range(24)
}

_MIN_PAD = {
    i: f'{i:02d}' for i in range(60)
}

_SEC_PAD = {
    i: f'{i:02d}' for i in range(60)
}

def format_datetime_iso(dt: datetime) -> str:
    if not isinstance(dt, datetime):
        raise ValueError("Input must be a datetime object")
    
    year = str(dt.year)
    month = _MONTH_PAD.get(dt.month, f'{dt.month:02d}')
    day = _DAY_PAD.get(dt.day, f'{dt.day:02d}')
    hour = _HOUR_PAD.get(dt.hour, f'{dt.hour:02d}')
    minute = _MIN_PAD.get(dt.minute, f'{dt.minute:02d}')
    second = _SEC_PAD.get(dt.second, f'{dt.second:02d}')
    
    return f"{year}-{month}-{day} {hour}:{minute}:{second}"

if __name__ == '__main__':
    sample_dt = datetime(2024, 1, 9, 8, 5, 3)
    result = format_datetime_iso(sample_dt)
    print(result)