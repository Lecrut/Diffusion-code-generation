from operator import itemgetter

def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=itemgetter(key))

if __name__ == '__main__':
    sample_data = [
        {'name': 'X', 'score': 85},
        {'name': 'Y', 'score': 92},
        {'name': 'Z', 'score': 78},
        {'name': 'W', 'score': 95}
    ]
    sorted_data = sort_dicts_by_key(sample_data, 'score')
    for entry in sorted_data:
        print(entry)