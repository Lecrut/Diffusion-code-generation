def validate_data(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list.")
    for item in data:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each item must be a tuple of two elements.")

def segment_by_sign(data):
    validate_data(data)
    positive = [item[1] for item in data if item[0] > 0]
    negative = [item[1] for item in data if item[0] < 0]
    zero = [item[1] for item in data if item[0] == 0]
    return {'positive': positive, 'negative': negative, 'zero': zero}

if __name__ == '__main__':
    sample_data = [
        (1, 'one'),
        (-2, 'two'),
        (3, 'three'),
        (-4, 'four'),
        (0, 'zero')
    ]
    segmented_data = segment_by_sign(sample_data)
    print(segmented_data)