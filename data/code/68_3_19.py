class DifferenceCalculator:
    @staticmethod
    def calculate(A, B):
        if len(A) != len(B):
            raise ValueError("Lists A and B must be of the same length.")
        return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [20, 30, 40]
    B = [10, 15, 20]
    try:
        differences = DifferenceCalculator.calculate(A, B)
        print(differences)
    except ValueError as e:
        print(e)