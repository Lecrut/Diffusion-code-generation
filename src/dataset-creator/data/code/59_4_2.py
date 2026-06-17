from datetime import date
def get_day_name(year, month, day):
    try:
        d = date(year, month, day)
        return str(d.strftime("%A")).lower()
    except ValueError as e:
        raise ValueError(f"Invalid date provided. {e}")
def map_date(year, month, day):
    try:
        d = date(year, month, day)
        _weekday_num = d.weekday() if hasattr(d, 'weekday') else None 
        return d
    except ValueError as e:
        raise ValueError(f"Invalid date provided. {e}")
if __name__ == '__main__':
    year_sample_1 = 2023
    month_sample_1 = 5
    day_sample_1 = 1
    result_name_1 = get_day_name(year_sample_1, month_sample_1, day_sample_1)
    year_sample_2 = 2024
    month_sample_2 = 7
    day_sample_2 = 4
    mapped_date_obj_1 = map_date(year_sample_1, month_sample_1, day_sample_1)
    print(f"Sample 1: {year_sample_1}-{month_sample_1:02d}-{day_sample_1:02d} is a {result_name_1}")
    print(f"Mapped Object (Sample 1): {mapped_date_obj_1.strftime('%A, %B %d, %Y')}")
    result_name_2 = get_day_name(year_sample_2, month_sample_2, day_sample_2)
    print(f"Sample 2: {year_sample_2}-{month_sample_2:02d}-{day_sample_2:02d} is a {result_name_2}")