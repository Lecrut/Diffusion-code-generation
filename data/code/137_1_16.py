class GradeClassifier:
    def classify(self, score):
        grades = ['F', 'D', 'C', 'B', 'A']
        bounds = [60, 70, 80, 90]
        for i, bound in enumerate(bounds):
            if score >= bound:
                return grades[i + 1]

if __name__ == '__main__':
    classifier = GradeClassifier()
    print(classifier.classify(95))
    print(classifier.classify(82))
    print(classifier.classify(70))
    print(classifier.classify(65))
    print(classifier.classify(55))