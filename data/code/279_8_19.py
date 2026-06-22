class PowerCycler:
    @staticmethod
    def cycle_and_square(numbers):
        return [number ** 2 for number in numbers]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    squared_values = PowerCycler.cycle_and_square(sample_values)
    print(squared_values)