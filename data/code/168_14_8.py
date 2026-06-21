def segment_tuples(data):
    positive = [item for item, sign in data if sign > 0]
    negative = [item for item, sign in data if sign < 0]
    return {'positive': positive, 'negative': negative}

if __name__ == '__main__':
    sample_data = [
        (10, -5),
        (-3, 2),
        (7, 4),
        (-8, -2),
        (6, 1)
    ]
    segmented_data = segment_tuples(sample_data)
    print(segmented_data)