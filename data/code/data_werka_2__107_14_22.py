from datetime import datetime, timedelta

SOURCE_FORMAT = '%d-%m-%Y %H:%M:%S'
TARGET_FORMAT = '%Y-%m-%dT%H:%M:%S'

def parse_and_reformat(date_input: str) -> str:
    year_str, month_str, rest = date_input.split('-')
    day_str, time_part = rest.split(' ')
    hour_str, minute_str, second_str = time_part.split(':')
    
    day_val = int(day_str)
    month_val = int(month_str)
    year_val = int(year_str)
    
    hour_val = int(hour_str)
    minute_val = int(minute_str)
    second_val = int(second_str)
    
    dt_obj = datetime(year_val, month_val, day_val, hour_val, minute_val, second_val)
    
    iso_date_part = f"{dt_obj.year:04d}-{dt_obj.month:02d}-{dt_obj.day:02d}"
    iso_time_part = f"{dt_obj.hour:02d}:{dt_obj.minute:02d}:{dt_obj.second:02d}"
    
    return f"{iso_date_part}T{iso_time_part}"

if __name__ == '__main__':
    raw_date = '31-07-2023 09:15:30'
    iso_output = parse_and_reformat(raw_date)
    print(iso_output)