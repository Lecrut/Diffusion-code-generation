class PowerCycler:
    def cycle_and_square(self, numbers):
        return [num ** 2 for num in numbers]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    power_cycler = PowerCycler()
    squared_values = power_cycler.cycle_and_square(sample_values)
    for value in squared_values:
        print(value)