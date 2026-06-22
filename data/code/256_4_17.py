class NumberCollection:
    def __init__(self, numbers):
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All elements must be integers or floats")
        self.numbers = numbers

    def get_range(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    try:
        sample_numbers = [10, 5, 20, 3]
        collection = NumberCollection(sample_numbers)
        print(f"Range: {collection.get_range()}")
    except ValueError as e:
        print(e)