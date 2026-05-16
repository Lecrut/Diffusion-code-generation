def sort_list_of_dicts(data):
    return sorted(data, key=lambda item: item['score'], reverse=True)
if __name__ == '__main__':
    data = [
        {'item': 'Apple', 'score': 85},
        {'item': 'Banana', 'score': 92},
        {'item': 'Cherry', 'score': 78},
        {'item': 'Date', 'score': 92},
        {'item': 'Elderberry', 'score': 88}
    ]
    sorted_data = sort_list_of_dicts(data)
    for item in sorted_data:
        print(item)