class RangeCycler:
    def cycle_and_print_evens(self, start, end):
        for num in range(start, end + 1):
            if num % 2 == 0:
                print(num)

if __name__ == '__main__':
    cycler = RangeCycler()
    start_val = 100
    end_val = 200
    cycler.cycle_and_print_evens(start_val, end_val)