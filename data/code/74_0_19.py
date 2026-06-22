import datetime

WEEKDAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def _validate_weekday_index(index: int) -> None:
    if not isinstance(index, int):
        raise TypeError("Index must be an integer.")
    if index < 0 or index > 6:
        raise ValueError("Index must be between 0 and 6.")

def get_weekday_name_from_index(index: int) -> str:
    _validate_weekday_index(index)
    return WEEKDAY_ORDER[index]

def get_current_day_name() -> str:
    today = datetime.date.today()
    current_index = today.weekday()
    return get_weekday_name_from_index(current_index)

if __name__ == '__main__':
    test_indices = [0, 6]
    for idx in test_indices:
        print(get_weekday_name_from_index(idx))
    print(get_current_day_name())