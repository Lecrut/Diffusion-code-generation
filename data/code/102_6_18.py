def is_weekday(day_index):
    if not isinstance(day_index, int) or day_index < 0 or day_index > 6:
        raise ValueError("Day index must be an integer between 0 and 6")
    return 1 <= day_index <= 5

if __name__ == '__main__':
    sample_days = [0, 1, 2, 3, 4, 5, 6]
    for day in sample_days:
        print(f"Day {day}: {'Weekday' if is_weekday(day) else 'Weekend'}")