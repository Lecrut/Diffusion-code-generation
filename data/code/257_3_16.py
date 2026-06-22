class ComplexNumberDifference:
    @staticmethod
    def calculate_difference(data):
        if len(data) < 2:
            raise ValueError("List must contain at least two elements to calculate the difference.")
        return max(data) - min(data)

if __name__ == '__main__':
    sample_values = [
        [1 + 2j, 3 + 4j, 5 + 6j],
        [10 + 20j, 30 + 40j],
        [-1 + 1j, -2 + 2j, -3 + 3j]
    ]
    
    for values in sample_values:
        try:
            result = ComplexNumberDifference.calculate_difference(values)
            print(f"Difference for {values}: {result}")
        except ValueError as e:
            print(f"Error for {values}: {e}")