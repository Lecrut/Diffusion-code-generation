class ComplexNumberDifference:
    @staticmethod
    def calculate_difference(data):
        if len(data) < 2:
            raise ValueError("List must contain at least two elements to calculate the difference.")
        return max(data).real - min(data).real

if __name__ == '__main__':
    sample1 = [3 + 4j, 1 + 1j, 5 + 6j]
    sample2 = [7 + 8j, 9 + 10j, 2 + 3j]
    sample3 = [11 + 12j, 13 + 14j, 15 + 16j]

    try:
        result1 = ComplexNumberDifference.calculate_difference(sample1)
        print(f"Difference for {sample1}: {result1}")
    except ValueError as e:
        print(f"Error for {sample1}: {e}")

    try:
        result2 = ComplexNumberDifference.calculate_difference(sample2)
        print(f"Difference for {sample2}: {result2}")
    except ValueError as e:
        print(f"Error for {sample2}: {e}")

    try:
        result3 = ComplexNumberDifference.calculate_difference(sample3)
        print(f"Difference for {sample3}: {result3}")
    except ValueError as e:
        print(f"Error for {sample3}: {e}")