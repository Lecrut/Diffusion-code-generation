def min_value_generator(numbers):
    if not numbers:
        raise ValueError("The input list cannot be empty")
    
    minimum = next(iter(numbers))
    for number in numbers:
        if number < minimum:
            minimum = number
        yield minimum

if __name__ == '__main__':
    data = [15, 3, 8, 22, 1]
    gen = min_value_generator(data)
    
    for _ in range(len(data)):
        print(next(gen))