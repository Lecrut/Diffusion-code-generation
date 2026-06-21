def segment_tuples(data):
    positive = [item for item in data if item[0] >= 0]
    negative = [item for item in data if item[0] < 0]
    return {'positive': positive, 'negative': negative}

if __name__ == '__main__':
    sample_data = [
        (1, 'apple'),
        (-2, 'carrot'),
        (3, 'banana'),
        (-4, 'broccoli'),
        (5, 'lettuce')
    ]
    segmented_data = segment_tuples(sample_data)
    print(segmented_data)