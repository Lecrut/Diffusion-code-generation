class OddNumberGenerator:
    def __init__(self, numbers):
        self.numbers = iter(numbers)
    
    def get_next_odd(self):
        while True:
            number = next(self.numbers)
            if number % 2 != 0:
                return number

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_gen = OddNumberGenerator(sample_list)
    print(odd_gen.get_next_odd())
    print(odd_gen.get_next_odd())
    print(odd_gen.get_next_odd())