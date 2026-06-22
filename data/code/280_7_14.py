class NumberClassifier:
    def classify(self, number):
        if number % 2 == 0:
            return f"{number} is even"
        else:
            return f"{number} is odd"

if __name__ == '__main__':
    classifier = NumberClassifier()
    for i in range(15):
        print(classifier.classify(i))