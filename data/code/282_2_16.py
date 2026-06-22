class NumberSummator:
    @staticmethod
    def sum_numbers(data):
        return sum(data)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    result = NumberSummator.sum_numbers(sample_values)
    print(result)