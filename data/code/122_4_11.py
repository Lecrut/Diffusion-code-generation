class Averager:
    def __init__(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be numeric")
        self.numbers = numbers

    @staticmethod
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

    def average(self):
        return Averager.calculate_average(self.numbers)

if __name__ == '__main__':
    try:
        data = [10, 20, 30, 40, 50]
        averager = Averager(data)
        print(averager.average())
    except ValueError as e:
        print(f"Error: {e}")