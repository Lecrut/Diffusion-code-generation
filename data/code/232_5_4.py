class GrowingNumberGenerator:
    def __init__(self):
        self.current = 0

    def get_next_number(self):
        if self.current > 99:
            raise ValueError("Sequence limit exceeded")
        else:
            number = self.current
            self.current += 1
            return number

if __name__ == '__main__':
    generator_instance = GrowingNumberGenerator()
    try:
        while True:
            print(generator_instance.get_next_number())
    except ValueError as e:
        print(e)