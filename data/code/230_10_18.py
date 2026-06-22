class NumberFilter:
    def filter_even_numbers(self, number_list):
        return [num for num in number_list if num % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6]
    filter_instance = NumberFilter()
    even_numbers = filter_instance.filter_even_numbers(sample_numbers)
    print(even_numbers)