class OddNumberGenerator:
    START = 1
    END = 101
    STEP = 2

    @staticmethod
    def generate_odd_numbers():
        return list(range(OddNumberGenerator.START, OddNumberGenerator.END, OddNumberGenerator.STEP))

if __name__ == '__main__':
    odd_numbers = OddNumberGenerator.generate_odd_numbers()
    print(odd_numbers)