def classify_day(day):
    if day in ('Saturday', 'Sunday'):
        return 'Weekend'
    elif isinstance(day, str):
        return 'Weekday'
    else:
        raise ValueError("Invalid input: expected a string representing a day of the week")

if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))
    print(classify_day('Sunday'))