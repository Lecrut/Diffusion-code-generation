class NumberCycler:
    START = 1
    END = 10

    @staticmethod
    def cycle_range(start, end):
        for i in range(start, end + 1):
            print(i)

if __name__ == '__main__':
    number_cycler = NumberCycler()
    number_cycler.cycle_range(NumberCycler.START, NumberCycler.END)