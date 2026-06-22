def find_extremes(numbers):
    if not numbers:
        return None, None
    
    smallest = largest = numbers[0]
    
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    
    return smallest, largest

if __name__ == '__main__':
    print(find_extremes([3, 1, 4, 1, 5, 9, 2]))
    print(find_extremes([-7, -1, -5, -3]))
    print(find_extremes([]))