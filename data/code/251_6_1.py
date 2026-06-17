def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
def largest_generator(iterable):
    it = iter(iterable)
    try:
        first_item = next(it)
        current_largest = first_item
    except StopIteration:
        return
    for number in it:
        if number > current_largest:
            current_largest = number
        yield current_largest
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    print(list(largest_generator(sample_data)))
    sample_data_2 = [5, -2, 8, -10, 1]
    print(list(largest_generator(sample_data_2)))
    sample_data_3 = []
    print(list(largest_generator(sample_data_3)))
    sample_data_4 = [42]
    print(list(largest_generator(sample_data_4)))