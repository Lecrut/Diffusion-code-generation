class EvenFilter:
    def filter_evens(self, number_list):
        return [num for num in number_list if num % 2 == 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_filter = EvenFilter()
    evens = even_filter.filter_evens(sample_numbers)
    for even_number in evens:
        print(even_number)