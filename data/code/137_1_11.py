class GradeClassifier:
    def classify(self, score):
        grades = ['F', 'D', 'C', 'B', 'A']
        for i in range(4, -1, -1):
            if score >= (90 - i * 10):
                return grades[i]
        return 'F'

if __name__ == '__main__':
    classifier = GradeClassifier()
    print(classifier.classify(95))
    print(classifier.classify(82))
    print(classifier.classify(70))
    print(classifier.classify(65))
    print(classifier.classify(55))