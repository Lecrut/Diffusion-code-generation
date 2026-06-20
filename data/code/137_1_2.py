class GradeClassifier:
    def classify(self, score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        else:
            return 'F'

if __name__ == '__main__':
    classifier = GradeClassifier()
    print(classifier.classify(95))
    print(classifier.classify(85))
    print(classifier.classify(75))
    print(classifier.classify(65))