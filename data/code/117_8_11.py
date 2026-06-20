class NumberOperations:
    @staticmethod
    def calculate_difference(a, b):
        return a - b

if __name__ == '__main__':
    ops = NumberOperations()
    print(f"Difference between 10 and 5: {ops.calculate_difference(10, 5)}")
    print(f"Difference between 3.5 and 2: {ops.calculate_difference(3.5, 2)}")