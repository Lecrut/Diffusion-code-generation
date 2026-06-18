from datetime import date
def map_date_to_day_of_week(year: int, month: int, day: int) -> str:
    try:
        input_date = date(year=year, month=month, day=day)
        weekday_number = input_date.weekday()
        days_of_week = [
            "Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday", 
            "Friday", 
            "Saturday", 
            "Sunday"
        ]
        return days_of_week[weekday_number]
    except ValueError as e:
        raise ValueError(f"Invalid date provided. Error details: {str(e)}")
if __name__ == '__main__':
    year_1 = 2024
    month_1 = 5
    day_1 = 3
    year_2 = 2024
    month_2 = 7
    day_2 = 4
    year_3 = 2025
    month_3 = 12
    day_3 = 31
    print("Date to Day of Week Mapper - Execution Log")
    print("-" * 40)
    result_1 = map_date_to_day_of_week(year_1, month_1, day_1)
    formatted_date_1 = f"{year_1}-{month_1:02d}-{day_1:02d}"
    print(f"Input Date ({formatted_date_1}): {result_1}")
    result_2 = map_date_to_day_of_week(year_2, month_2, day_2)
    formatted_date_2 = f"{year_2}-{month_2:02d}-{day_2:02d}"
    print(f"Input Date ({formatted_date_2}): {result_2}")
    result_3 = map_date_to_day_of_week(year_3, month_3, day_3)
    formatted_date_3 = f"{year_3}-{month_3:02d}-{day_3:02d}"
    print(f"Input Date ({formatted_date_3}): {result_3}")
    try:
        result_error = map_date_to_day_of_week(2024, 2, 31)
    except ValueError as e:
        print(f"Error Handling Test Failed Date Input ({'2024-02-31'}): {e}")
    print("-" * 40)