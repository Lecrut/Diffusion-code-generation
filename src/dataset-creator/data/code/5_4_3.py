def difference_largest_smallest(numbers):
    if not numbers:
        return 0
    smallest = numbers[0]
    largest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
    return largest - smallest
if __name__ == '__main__':
    sample_list = [15, 3, 8, 22, 1]
    result = difference_largest_smallest(sample_list)
    print(result)