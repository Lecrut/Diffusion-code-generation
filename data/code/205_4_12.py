from operator import itemgetter

ASCENDING = False

def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=itemgetter(key), reverse=ASCENDING)

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = sort_dicts_by_key(sample_dicts, 'age')
    print(sorted_dicts)