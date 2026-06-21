def find_second_smallest_largest(numbers):
    if len(numbers) < 2:
        return (None, None)
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    for number in numbers:
        if number < smallest:
            second_smallest, smallest = (smallest, number)
        elif smallest < number < second_smallest:
            second_smallest = number
        if number > largest:
            second_largest, largest = (largest, number)
        elif largest > number > second_largest:
            second_largest = number
    return (second_smallest if second_smallest != float('inf') else None, second_largest if second_largest != float('-inf') else None)
if __name__ == '__main__':
    sample_numbers = [4, 2, 9, 7, 5, 1, 8, 3, 6]
    print(find_second_smallest_largest(sample_numbers))