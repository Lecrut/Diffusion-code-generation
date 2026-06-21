from operator import itemgetter

def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=itemgetter(key))

if __name__ == '__main__':
    sample_data = [
        {'id': 3, 'score': 85},
        {'id': 1, 'score': 92},
        {'id': 2, 'score': 78},
        {'id': 4, 'score': 90}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'score')
    print(sorted_data)