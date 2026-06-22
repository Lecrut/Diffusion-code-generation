from datetime import date

def is_weekday(d: date) -> bool:
    weekday_index = d.weekday()
    is_monday = weekday_index == 0
    is_tuesday = weekday_index == 1
    is_wednesday = weekday_index == 2
    is_thursday = weekday_index == 3
    is_friday = weekday_index == 4
    return is_monday or is_tuesday or is_wednesday or is_thursday or is_friday

if __name__ == '__main__':
    test_date = date(2024, 7, 4)
    result = is_weekday(test_date)
    print(result)