def get_value_at_index(generator, index):
    current_index = 0
    for value in generator:
        if current_index == index:
            return value
        current_index += 1
    raise IndexError("index out of range")

if __name__ == '__main__':
    sample_generator = (x * x for x in range(10))
    target_index = 5
    result = get_value_at_index(sample_generator, target_index)
    print(result)