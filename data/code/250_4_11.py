class AverageCalculator:
    @staticmethod
    def calculate_average(values):
        total = 0
        count = 0
        for value in values:
            total += value
            count += 1
            yield (total / count)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    avg_gen = AverageCalculator.calculate_average(sample_values)
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))