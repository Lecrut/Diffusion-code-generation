def even_numbers():
    for i in range(2, 101, 2):
        yield i

class NumberProcessor:
    def __init__(self, start=1, end=100):
        self.start = start
        self.end = end
    
    def is_even(self, number):
        return number % 2 == 0
    
    def process_numbers(self):
        for num in range(self.start, self.end + 1):
            if self.is_even(num):
                yield num

if __name__ == '__main__':
    processor = NumberProcessor()
    for even_number in processor.process_numbers():
        print(even_number)