from datetime import date
def map_date_to_day(year, month, day):
    try:
        d = date(year, month, day)
        return d.strftime("%A")
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {year}-{month}-{day}. Error details: {e}")
if __name__ == '__main__':
    year = 2023
    month = 10
    day = 5
    result_day_name = map_date_to_day(year, month, day)
    print(f"Date: {year}-{month:02d}-{day:02d}")
    print("Day of Week:", result_day_name)