def sign(x):
    return (x > 0) - (x < 0)

def segment_tuples(data):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in data):
        raise ValueError("All elements must be tuples of length 2")
    
    if not all(isinstance(item[1], int) for item in data):
        raise ValueError("Second element of each tuple must be an integer")
    
    return [list(group) for _, group in sorted(((sign(item[0]), item) for item in data))]

if __name__ == '__main__':
    sample_data = [
        (3, 1),
        (-1, 2),
        (2, 3),
        (-2, 4)
    ]
    segmented_data = segment_tuples(sample_data)
    print(segmented_data)