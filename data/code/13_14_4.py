def get_value_at_index(gen, index):
    if index < 0:
        raise IndexError("index cannot be negative")
    current_index = 0
    for value in gen:
        if current_index == index:
            return value
        current_index += 1
    raise IndexError(f"index {index} out of range")

if __name__ == '__main__':
    sample_generator = (x * x for x in range(100))
    result = get_value_at_index(sample_generator, 10)
    print(result)