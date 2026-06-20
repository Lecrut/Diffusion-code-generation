class NegativityChecker:
    @staticmethod
    def check_negativity(value):
        return value < 0

if __name__ == '__main__':
    input_data = [10, -5, 20, -1, 33, -12, 0]
    for number in input_data:
        if NegativityChecker.check_negativity(number):
            print(number)