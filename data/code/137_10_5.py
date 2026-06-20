class DayClassifier:
    def classify_day(self, day):
        return 'Weekend' if day in ('Saturday', 'Sunday') else 'Weekday'

if __name__ == '__main__':
    classifier = DayClassifier()
    print(classifier.classify_day('Saturday'))
    print(classifier.classify_day('Monday'))