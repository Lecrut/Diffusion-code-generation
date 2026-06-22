def min_value_generator(data):
    if not data:
        raise ValueError("Data cannot be empty")
    yield from (x for x in data)
    
if __name__ == '__main__':
    sample_data = [15, 3, 8, 22, 1]
    gen = min_value_generator(sample_data)
    minimum = next(gen)
    for number in gen:
        if number < minimum:
            minimum = number
    print(minimum)