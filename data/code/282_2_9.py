class NumberSummator:
    def sum_sequence(self, numbers):
        return sum(numbers)

if __name__ == '__main__':
    summator = NumberSummator()
    sample_values = [1, 2, 3, 4, 5]
    result = summator.sum_sequence(sample_values)
    print(result)