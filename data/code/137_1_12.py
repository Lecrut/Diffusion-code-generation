class GradeClassifier:
    def classify(self, score):
        if not isinstance(score, (int, float)) or score < 0:
            raise ValueError("Score must be a non-negative number")
        return 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else 'F'))

if __name__ == '__main__':
    classifier = GradeClassifier()
    print(classifier.classify(95))
    print(classifier.classify(82))
    print(classifier.classify(70))
    print(classifier.classify(65))
    print(classifier.classify(55))