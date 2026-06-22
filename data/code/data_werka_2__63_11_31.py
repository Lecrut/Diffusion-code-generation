def get_first_item(iterable):
    iterator = iter(iterable)
    try:
        first_item = next(iterator)
    except StopIteration:
        raise ValueError('The iterable is empty')
    return first_item

if __name__ == '__main__':
    sample_data = [
        [10, 20, 30],
        (40, 50, 60),
        'hello',
        {70, 80, 90}
    ]
    
    for index, data in enumerate(sample_data):
        try:
            result = get_first_item(data)
            print(f"First item of sample {index + 1}: {result}")
        except ValueError as e:
            print(f"Error for sample {index + 1}: {e}")