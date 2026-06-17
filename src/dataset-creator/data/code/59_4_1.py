def get_day_of_week(year: int, month: int, day: int) -> str:
    from datetime import date
    try:
        d = date(year, month, day)
        return d.strftime('%A')
    except ValueError as e:
        raise ValueError(f"Invalid date provided: {year}-{month}-{day}. Error details: {e}")
if __name__ == '__main__':
    year_1 = 2023
    month_1 = 10
    day_1 = 27
    year_2 = 2024
    month_2 = 6
    day_2 = 15
    year_3 = 1969
    month_3 = 7
    day_3 = 20
    print(f"Date: {year_1}-{month_1}-{day_1} is a {get_day_of_week(year_1, month_1, day_1)}")
    print(f"Date: {year_2}-{month_2}-{day_2} is a {get_day_of_week(year_2, month_2, day_2)}")
    print(f"Date: {year_3}-{month_3}-{day_3} is a {get_day_of_week(year_3, month_3, day_3)}")