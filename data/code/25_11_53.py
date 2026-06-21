class EvenNumberGenerator:
    @staticmethod
    def is_even(num):
        return num % 2 == 0

    @staticmethod
    def is_zero(num):
        return num == 0

    def generate(self, start, end):
        for num in range(start, end + 1):
            if self.is_even(num) and (self.is_zero(num) or not self.is_zero(num)):
                yield True if self.is_zero(num) else False

if __name__ == '__main__':
    generator = EvenNumberGenerator()
    start_value = -3
    end_value = 7
    for result in generator.generate(start_value, end_value):
        print(result)