class NumberClassifier:
    @staticmethod
    def is_odd(number):
        return number % 2 == 1

if __name__ == '__main__':
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for num in test_numbers:
        if NumberClassifier.is_odd(num):
            print(f"{num} is Odd")
        else:
            print(f"{num} is Even")