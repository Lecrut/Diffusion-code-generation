def is_weekend(day):
    return day in ('Saturday', 'Sunday')

def classify_day(day):
    if not isinstance(day, str):
        raise ValueError("Input must be a string representing a day of the week.")
    
    if is_weekend(day):
        return 'Weekend'
    else:
        return 'Weekday'

if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))