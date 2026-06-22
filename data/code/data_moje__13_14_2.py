def get_generator_value_at_index(gen, index):
    if index < 0:
        raise IndexError("index must be non-negative")
    for current_index, value in enumerate(gen):
        if current_index == index:
            return value
    raise IndexError("index out of range")

if __name__ == '__main__':
    numbers = (x * x for x in range(10))
    result = get_generator_value_at_index(numbers, 5)
    print(result)