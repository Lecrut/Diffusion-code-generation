class NumberProcessor:
    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers) if numbers else 0

if __name__ == '__main__':
    processor = NumberProcessor()
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15, 25]
    data3 = []
    print(f"Average of {data1}: {processor.calculate_average(data1)}")
    print(f"Average of {data2}: {processor.calculate_average(data2)}")
    print(f"Average of {data3}: {processor.calculate_average(data3)}")