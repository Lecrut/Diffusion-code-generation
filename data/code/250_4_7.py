def average_generator(values):
    total = 0
    count = 0
    for value in values:
        if not isinstance(value, (int, float)):
            raise ValueError("All elements must be numbers")
        total += value
        count += 1
        yield total / count

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    avg_gen = average_generator(sample_values)
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))
    print(next(avg_gen))