class NumberClassifier:
    @staticmethod
    def is_even(number):
        return number & 1 == 0

if __name__ == '__main__':
    classifier = NumberClassifier()
    print(f"4 is even: {classifier.is_even(4)}")
    print(f"5 is even: {classifier.is_even(5)}")
    print(f"0 is even: {classifier.is_even(0)}")
    print(f"-2 is even: {classifier.is_even(-2)}")
    print(f"-3 is even: {classifier.is_even(-3)}")