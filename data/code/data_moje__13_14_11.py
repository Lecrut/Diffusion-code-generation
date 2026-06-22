def get_value_at_index(generator, index):
    for current_index, value in enumerate(generator):
        if current_index == index:
            return value
    raise IndexError("index out of range")

if __name__ == '__main__':
    sample_generator = (x * x for x in range(10))
    result = get_value_at_index(sample_generator, 5)
    print(result)