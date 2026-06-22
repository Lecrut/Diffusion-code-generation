def find_extremes(numbers):
    if not numbers:
        return None
    smallest = largest = numbers[0]
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    return (smallest, largest)

if __name__ == '__main__':
    sample_list = [54, 23, 89, 67, 12, 90]
    extremes = find_extremes(sample_list)
    print(f"Smallest value: {extremes[0]}")
    print(f"Largest value: {extremes[1]}")