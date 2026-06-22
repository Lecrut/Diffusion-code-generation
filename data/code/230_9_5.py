def filter_divisible_by_three(numbers):
    return list(filter(lambda x: x % 3 == 0, numbers))

class NumberFilter:
    def __init__(self, values):
        self.values = values

    def get_filtered_values(self):
        return filter_divisible_by_three(self.values)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_filter = NumberFilter(sample_values)
    filtered_values = number_filter.get_filtered_values()
    print(filtered_values)