def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest
def largest_generator(iterable):
    try:
        iterator = iter(iterable)
        first = next(iterator)
        largest = first
        for number in iterator:
            if number > largest:
                largest = number
        yield largest
    except StopIteration:
        return
if __name__ == '__main__':
    sample_data1 = [10, 5, 20, 8, 15]
    print(list(largest_generator(sample_data1)))
    sample_data2 = [-5, -1, -10, -3]
    print(list(largest_generator(sample_data2)))
    sample_data3 = [42]
    print(list(largest_generator(sample_data3)))
    sample_data4 = []
    print(list(largest_generator(sample_data4)))