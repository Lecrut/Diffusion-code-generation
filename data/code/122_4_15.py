class Averager:
    def __init__(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be numeric")
        self.numbers = numbers

    @staticmethod
    def from_string(input_data):
        try:
            numbers = [float(x) for x in input_data.split()]
            return Averager(numbers)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return None

    def compute_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    input_data = "10 20 30 40 50"
    averager = Averager.from_string(input_data)
    if averager:
        average = averager.compute_average()
        print(average)