class NumberClassifier:
    MAX_ITERATIONS = 15

    @staticmethod
    def classify(number):
        if number % 2 == 0:
            return f"{number} is even"
        else:
            return f"{number} is odd"

    @classmethod
    def run(cls):
        for i in range(cls.MAX_ITERATIONS):
            print(cls.classify(i))

if __name__ == '__main__':
    NumberClassifier.run()