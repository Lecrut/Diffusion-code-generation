def count_items_starting_at_zero(data: list) -> int:
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    return sum(1 for item in data if item == 0)
if __name__ == '__main__':
    sample_data = [0, 'a', False, [], {}, 0.0]
    result: int = count_items_starting_at_zero(sample_data)
    print(result)