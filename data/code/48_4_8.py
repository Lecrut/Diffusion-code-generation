def get_largest_generator(data):
    for item in data:
        yield item

def find_max_in_generator(data):
    iterator = get_largest_generator(data)
    try:
        max_val = next(iterator)
        for val in iterator:
            if val > max_val:
                max_val = val
    except StopIteration:
        return None
    return max_val

if __name__ == '__main__':
    sample_data = [10, 42, 7, 89, 23, 15, 98, 4, 61]
    result = find_max_in_generator(sample_data)
    print(result)