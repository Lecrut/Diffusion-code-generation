class NumberAverager:
    @staticmethod
    def calculate_average(numbers):
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    average = NumberAverager.calculate_average(sample_list)
    print(average)