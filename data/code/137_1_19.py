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
    sample_scores = [95, 82, 68, 55]
    for score in sample_scores:
        print(f"Score: {score}, Grade: {classifier.classify(score)}")