def classify_day(day):
    return 'Weekend' if day in ('Saturday', 'Sunday') else 'Weekday'
if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))