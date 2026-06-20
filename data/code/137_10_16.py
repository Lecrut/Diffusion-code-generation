class DayClassifier:
    WEEKEND_DAYS = ('Saturday', 'Sunday')

    @staticmethod
    def classify(day):
        return 'Weekend' if day in DayClassifier.WEEKEND_DAYS else 'Weekday'

if __name__ == '__main__':
    print(DayClassifier.classify('Saturday'))
    print(DayClassifier.classify('Monday'))