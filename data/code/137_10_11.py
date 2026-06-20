def classify_day(day):
    if day in ('Saturday', 'Sunday'):
        return 'Weekend'
    else:
        return 'Weekday'

if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))