from calendar import monthrange

def determine_weekday(year, month, day):
    _, weekday = monthrange(year, month)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return days[weekday]
if __name__ == '__main__':
    print(determine_weekday(2023, 10, 26))
    print(determine_weekday(2024, 1, 1))
    print(determine_weekday(2025, 12, 31))