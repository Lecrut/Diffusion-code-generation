class OddNumberGenerator:
    START = 1
    END = 101
    STEP = 2

    @staticmethod
    def generate():
        return list(range(OddNumberGenerator.START, OddNumberGenerator.END, OddNumberGenerator.STEP))

if __name__ == '__main__':
    odd_numbers = OddNumberGenerator.generate()
    print(odd_numbers)