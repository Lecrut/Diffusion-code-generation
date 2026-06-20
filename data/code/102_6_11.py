def is_weekday(day_index):
    return 0 <= day_index < 5

if __name__ == '__main__':
    day1 = 2
    day2 = 5
    day3 = 6
    print(f"Day {day1} (Monday):", is_weekday(day1))
    print(f"Day {day2} (Saturday):", is_weekday(day2))
    print(f"Day {day3} (Sunday):", is_weekday(day3))