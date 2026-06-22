class NumberCycler:
    def cycle_even_numbers(self):
        for num in range(100):
            if num % 2 == 0:
                print(num)

if __name__ == '__main__':
    cycler = NumberCycler()
    cycler.cycle_even_numbers()