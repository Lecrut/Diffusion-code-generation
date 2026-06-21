class MinFinder:
    @staticmethod
    def find_minimum(numbers):
        if not numbers:
            return None
        minimum = numbers[0]
        for number in numbers:
            if number < minimum:
                minimum = number
        return minimum

if __name__ == '__main__':
    sample_values = [1, 5, 2, 8], [-10, -5, -20, -1], [3.14, 1.618, 2.718], [-5, 0, 5, -10], [7], []
    for values in sample_values:
        print(MinFinder.find_minimum(values))