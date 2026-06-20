def classify_day(day):
    if not isinstance(day, str) or day not in ('Saturday', 'Sunday'):
        raise ValueError("Invalid input: Day must be either 'Saturday' or 'Sunday'")
    return 'Weekend' if day in ('Saturday', 'Sunday') else 'Weekday'
if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))