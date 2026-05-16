from datetime import date
def date_to_weekday_info(dt: date) -> tuple[str, int]:
    weekday_names = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    weekday_index = dt.weekday()
    day_name = weekday_names[weekday_index]
    day_number = weekday_index + 1
    return day_name, day_number
if __name__ == '__main__':
    sample_date_1 = date(2023, 10, 25)
    sample_date_2 = date(2024, 1, 1)
    sample_date_3 = date(2024, 12, 25)
    result1 = date_to_weekday_info(sample_date_1)
    print(f"Date: {sample_date_1}, Result: {result1}")
    result2 = date_to_weekday_info(sample_date_2)
    print(f"Date: {sample_date_2}, Result: {result2}")
    result3 = date_to_weekday_info(sample_date_3)
    print(f"Date: {sample_date_3}, Result: {result3}")