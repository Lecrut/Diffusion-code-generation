def find_extremes(numbers):
    if not numbers:
        raise ValueError("List is empty")
    
    smallest = largest = numbers[0]
    
    for number in numbers[1:]:
        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
    
    return (smallest, largest)

if __name__ == '__main__':
    print(find_extremes([5, 3, 9, 1, 10]))