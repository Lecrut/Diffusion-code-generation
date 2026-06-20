def filter_and_sort(data, min_score):
    filtered = [item for item in data if item['score'] >= min_score]
    sorted_data = sorted(filtered, key=lambda x: x['score'], reverse=True)
    return sorted_data

if __name__ == '__main__':
    sample_data = [
        {'item': 'Apple', 'score': 85},
        {'item': 'Banana', 'score': 92},
        {'item': 'Cherry', 'score': 78},
        {'item': 'Date', 'score': 92},
        {'item': 'Elderberry', 'score': 88}
    ]
    result = filter_and_sort(sample_data, min_score=80)
    print(result)