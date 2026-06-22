class RangeCycler:
    def cycle_evens(self):
        evens = [num for num in range(100, 201) if num % 2 == 0]
        return evens

if __name__ == '__main__':
    cycler = RangeCycler()
    even_numbers = cycler.cycle_evens()
    print(even_numbers)