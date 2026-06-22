class Statistics:
    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    numbers = [10, 20, 30, 40]
    avg = Statistics.calculate_average(numbers)
    print(avg)