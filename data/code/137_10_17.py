WEEKEND_DAYS = ('Saturday', 'Sunday')

def classify_day(day):
    return 'Weekend' if day in WEEKEND_DAYS else 'Weekday'

if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))