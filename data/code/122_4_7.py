class Averager:
    def __init__(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be numeric")
        self.numbers = numbers

    def average(self):
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    try:
        avg = Averager([10, 20, 30, 40, 50])
        print(avg.average())
    except ValueError as e:
        print(e)