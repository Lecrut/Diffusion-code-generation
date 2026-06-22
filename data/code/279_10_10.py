class NumberCycler:
    START = 1
    END = 10

    @staticmethod
    def cycle_numbers():
        for number in range(NumberCycler.START, NumberCycler.END + 1):
            print(number)

if __name__ == '__main__':
    NumberCycler.cycle_numbers()