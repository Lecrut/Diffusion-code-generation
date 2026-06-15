class MathUtils:
    @staticmethod
    def calculate_mean(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
if __name__ == '__main__':
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    data3 = []
    print(f"Mean of {data1}: {MathUtils.calculate_mean(data1)}")
    print(f"Mean of {data2}: {MathUtils.calculate_mean(data2)}")
    print(f"Mean of {data3}: {MathUtils.calculate_mean(data3)}")