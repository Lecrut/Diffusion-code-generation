class Averager:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    sample_numbers = "15 25 35 45 55"
    try:
        numbers_list = [int(x) for x in sample_numbers.split()]
        averager_instance = Averager(numbers_list)
        average_result = averager_instance.calculate_average()
        print(average_result)
    except ValueError:
        print("Error: Input contains non-numeric values.")