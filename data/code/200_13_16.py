class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def square_numbers(self):
        return [x**2 for x in self.numbers]

if __name__ == '__main__':
    processor = NumberProcessor([1, 2, 3, 4, 5])
    squared_result = processor.square_numbers()
    print(squared_result)