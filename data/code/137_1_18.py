class GradeClassifier:
    GRADE_A = 90
    GRADE_B = 80
    GRADE_C = 70
    GRADE_D = 60

    @staticmethod
    def classify(score):
        if score >= GradeClassifier.GRADE_A:
            return 'A'
        elif score >= GradeClassifier.GRADE_B:
            return 'B'
        elif score >= GradeClassifier.GRADE_C:
            return 'C'
        elif score >= GradeClassifier.GRADE_D:
            return 'D'
        else:
            return 'F'

if __name__ == '__main__':
    classifier = GradeClassifier()
    print(classifier.classify(95))
    print(classifier.classify(82))
    print(classifier.classify(70))
    print(classifier.classify(65))