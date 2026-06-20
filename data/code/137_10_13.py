class DayClassifier:
    def classify(self, day):
        return 'Weekend' if day in ('Saturday', 'Sunday') else 'Weekday'

if __name__ == '__main__':
    classifier = DayClassifier()
    print(classifier.classify('Saturday'))
    print(classifier.classify('Monday'))