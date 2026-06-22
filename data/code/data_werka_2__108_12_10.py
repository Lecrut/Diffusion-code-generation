from datetime import datetime

def get_day_component(timestamp: str) -> int:
    date_part = timestamp.split('T')[0]
    year_str, month_str, day_str = date_part.split('-')
    return int(day_str)

if __name__ == '__main__':
    sample_ts = '2024-07-04T12:00:00'
    day_value = get_day_component(sample_ts)
    print(day_value)