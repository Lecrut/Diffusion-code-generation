class EvenNumberFilter:
    def filter_even_numbers(self, numbers):
        return {num for num in numbers if num > 10 and num % 2 == 0}

if __name__ == '__main__':
    sample_numbers = {8, 15, 20, 7, 12}
    filter_instance = EvenNumberFilter()
    result = filter_instance.filter_even_numbers(sample_numbers)
    print(result)