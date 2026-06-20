class NumberChecker:
    @staticmethod
    def verify_oddity(num):
        return num % 2 != 0

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = {value: NumberChecker.verify_oddity(value) for value in sample_values}
    print(results)