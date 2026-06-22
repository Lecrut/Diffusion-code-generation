def get_value_at_index(gen, index):
    try:
        for current_index, value in enumerate(gen):
            if current_index == index:
                return value
    except StopIteration:
        raise IndexError("index out of range")
    raise IndexError("index out of range")

if __name__ == '__main__':
    sample_gen = (x * x for x in range(10))
    target_index = 5
    result = get_value_at_index(sample_gen, target_index)
    print(result)