class OddNumberChecker:
    @staticmethod
    def is_odd(num):
        return num & 1 == 1

if __name__ == '__main__':
    test_values = [7, 23, 45, 68]
    results = {num: OddNumberChecker.is_odd(num) for num in test_values}
    print(results)