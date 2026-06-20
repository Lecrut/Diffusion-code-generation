DAY_MAP = {'Saturday': 'Weekend', 'Sunday': 'Weekend'}

def classify_day(day):
    return DAY_MAP.get(day, 'Weekday')

if __name__ == '__main__':
    print(classify_day('Saturday'))
    print(classify_day('Monday'))