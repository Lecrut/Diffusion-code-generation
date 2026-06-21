class MeanCalculator:
    def calculate_mean(self, data):
        return sum(data) / len(data)

if __name__ == '__main__':
    calculator = MeanCalculator()
    numbers1 = [1, 2, 3, 4, 5]
    numbers2 = [10.5, 20.5, 30.5]
    print(f"Mean of {numbers1}: {calculator.calculate_mean(numbers1)}")
    print(f"Mean of {numbers2}: {calculator.calculate_mean(numbers2)}")