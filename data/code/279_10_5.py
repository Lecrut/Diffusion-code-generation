class NumberCycler:
    def cycle_range(self, start, end):
        for i in range(start, end + 1):
            print(i)

if __name__ == '__main__':
    cycler = NumberCycler()
    sample_start = 1
    sample_end = 10
    cycler.cycle_range(sample_start, sample_end)