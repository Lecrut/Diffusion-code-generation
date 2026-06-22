def is_weekday(day_index):
    day_types = {
        0: "weekday",
        1: "weekday",
        2: "weekday",
        3: "weekday",
        4: "weekday",
        5: "weekend",
        6: "weekend"
    }
    if day_index not in day_types:
        raise ValueError(f"Index {day_index} out of range 0-6")
    return day_types[day_index] == "weekday"

if __name__ == '__main__':
    print(is_weekday(0))
    print(is_weekday(4))
    print(is_weekday(5))
    print(is_weekday(6))
    try:
        is_weekday(7)
    except ValueError as e:
        print(e)