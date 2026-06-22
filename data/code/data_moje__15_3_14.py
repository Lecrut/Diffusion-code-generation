def retrieve_penultimate_value(items):
    total_count = len(items)
    if total_count < 2:
        raise IndexError("Sequence must have at least two elements")
    target_index = total_count - 2
    return items[target_index]

if __name__ == '__main__':
    sample_integers = [7, 14, 21, 28, 35]
    penultimate_item = retrieve_penultimate_value(sample_integers)
    print(penultimate_item)