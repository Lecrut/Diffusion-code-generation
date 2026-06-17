from datetime import date
def map_date_to_day_of_week(year: int, month: int, day: int) -> str:
    try:
        input_date = date(year, month, day)
        return input_date.strftime('%A')                                                         
    except ValueError as ve:
        raise ValueError(f"Invalid date combination provided. Error details: {ve}")
if __name__ == '__main__':
    result_1 = map_date_to_day_of_week(2024, 1, 1)
    result_2 = map_date_to_day_of_week(2024, 7, 4)
    result_3 = map_date_to_day_of_week(2050, 1, 1)
    print(f"Date: {result_1}")
    print(f"Date: {result_2}")
    print(f"Date: {result_3}")