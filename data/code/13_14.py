def get_value_at_index(iterable, index):
    current_index = 0
    for value in iterable:
        if current_index == index:
            return value
        current_index += 1
    raise IndexError("index out of range")

if __name__ == '__main__':
    def generate_numbers():
        for i in range(10):
            yield i * 2

    sample_generator = generate_numbers()
    target_index = 3
    result = get_value_at_index(sample_generator, target_index)
    print(result)