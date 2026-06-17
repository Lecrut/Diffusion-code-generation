def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers[1:]:
        if number > largest:
            largest = number
    return largest
def largest_generator(iterable):
    it = iter(iterable)
    try:
        first = next(it)
        current_largest = first
    except StopIteration:
        return
    for number in it:
        if number > current_largest:
            current_largest = number
        yield current_largest
if __name__ == '__main__':
    sample_data = [10, 5, 20, 3, 15, 25]
    print(list(largest_generator(sample_data)))