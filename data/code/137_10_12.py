def classify_day(day):
    return 'Weekend' if day == 'Saturday' or day == 'Sunday' else 'Weekday'

if __name__ == '__main__':
    test_days = ['Monday', 'Tuesday', 'Friday', 'Saturday', 'Sunday']
    results = [classify_day(day) for day in test_days]
    print(results)