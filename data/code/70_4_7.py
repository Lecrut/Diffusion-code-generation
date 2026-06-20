class NumberProcessor:
    def __init__(self, input_string):
        self.numbers = list(map(int, input_string.split()))
    
    def get_first_last(self):
        if self.numbers:
            return self.numbers[0], self.numbers[-1]
        else:
            return None, None

if __name__ == '__main__':
    processor = NumberProcessor("10 20 30 40 50")
    first_number, last_number = processor.get_first_last()
    print(first_number, last_number)