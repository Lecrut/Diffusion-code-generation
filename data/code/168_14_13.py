def segment_tuples(data):
    result = [[], []]
    for item, sign in data:
        result[sign > 0].append(item)
    return result

if __name__ == '__main__':
    sample_data = [
        (1, 'positive'),
        (-1, 'negative'),
        (2, 'positive'),
        (-3, 'negative'),
        (4, 'positive')
    ]
    segmented_data = segment_tuples(sample_data)
    print(segmented_data)