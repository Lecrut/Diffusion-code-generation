def sort_items(data):
    return sorted(data, key=lambda item: item['score'], reverse=True)
if __name__ == '__main__':
    data = [
        {'item': 'Apple', 'score': 85},
        {'item': 'Banana', 'score': 92},
        {'item': 'Cherry', 'score': 78},
        {'item': 'Date', 'score': 92},
        {'item': 'Elderberry', 'score': 88}
    ]
    sorted_data = sort_items(data)
    print(sorted_data)