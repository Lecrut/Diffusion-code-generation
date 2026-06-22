def find_extremes(numbers):
    if not numbers:
        raise ValueError("The tuple is empty.")
    
    smallest = largest = numbers[0]
    
    for number in numbers:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    
    return smallest, largest

if __name__ == '__main__':
    sample_tuple = (15, -3, 88, -42, 99, 1)
    try:
        result = find_extremes(sample_tuple)
        print(f"Input Tuple: {sample_tuple}")
        print(f"Smallest value: {result[0]}")
        print(f"Largest value: {result[1]}")
    except ValueError as e:
        print(e)