class OddNumberGenerator:
    def __init__(self, numbers):
        self.numbers = iter(numbers)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            number = next(self.numbers)
            if number % 2 != 0:
                return number

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_gen = OddNumberGenerator(sample_list)
    for _ in range(len(sample_list) // 2):
        print(next(odd_gen))