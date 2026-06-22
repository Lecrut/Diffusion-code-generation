def sum_of_nines():

    def is_valid_input(numbers):
        if not isinstance(numbers, list) or len(numbers) != 9:
            raise ValueError('Input must be a list of exactly nine integers.')
        for num in numbers:
            if not isinstance(num, int):
                raise TypeError('All elements must be integers.')

    def calculate_sum(numbers):
        return sum(numbers)
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    is_valid_input(sample_numbers)
    result = calculate_sum(sample_numbers)
    print(result)
if __name__ == '__main__':
    sum_of_nines()