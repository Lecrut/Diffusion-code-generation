class NumberClassifier:
    @staticmethod
    def is_even(number):
        return number & 1 == 0

if __name__ == '__main__':
    classifier = NumberClassifier()
    print(f"Number 4 is even: {classifier.is_even(4)}")
    print(f"Number 5 is even: {classifier.is_even(5)}")
    print(f"Number -6 is even: {classifier.is_even(-6)}")
    print(f"Number -7 is even: {classifier.is_even(-7)}")