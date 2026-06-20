class GradeClassifier:
    def classify(self, score):
        return 'A' if score >= 90 else ('B' if score >= 80 else ('C' if score >= 70 else 'F'))

if __name__ == '__main__':
    classifier = GradeClassifier()
    scores = [95, 82, 70, 65, 55]
    for score in scores:
        print(f'Score: {score}, Grade: {classifier.classify(score)}')