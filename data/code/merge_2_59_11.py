import calendar
def get_weekday(year: int, month: int, day: int) -> int:
    return (calendar.weekday(year, month, day)) + 1
if __name__ == '__main__':
    sample_data = [
        (2023, 5, 1),
        (2024, 1, 1),
        (2024, 6, 15)
    ]
    for year, month, day in sample_data:
        result = get_weekday(year, month, day)
        print(f"{year}-{month:02d}-{day:02d} is weekday {result}")