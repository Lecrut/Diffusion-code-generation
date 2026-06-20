class GradeClassifier:
    GRADE_BOUNDARIES = {
        'A': 90,
        'B': 80,
        'C': 70,
        'D': 60
    }

    @staticmethod
    def classify(score):
        for grade, boundary in GradeClassifier.GRADE_BOUNDARIES.items():
            if score >= boundary:
                return grade
        return 'F'

if __name__ == '__main__':
    classifier = GradeClassifier()
    print(classifier.classify(95))
    print(classifier.classify(82))
    print(classifier.classify(70))
    print(classifier.classify(65))
    print(classifier.classify(55))