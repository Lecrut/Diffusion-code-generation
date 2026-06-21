class NumberFilter:
    @staticmethod
    def filter_even_numbers(mixed_list):
        return [item for item in mixed_list if isinstance(item, int) and item % 2 == 0]

if __name__ == '__main__':
    sample_values = [1, 2, 'a', 3, 4.5, 6]
    filter_instance = NumberFilter()
    even_numbers = filter_instance.filter_even_numbers(sample_values)
    print(even_numbers)