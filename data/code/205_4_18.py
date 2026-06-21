from operator import itemgetter
SORT_KEY = 'value'

def sort_dicts_by_key(dicts):
    return sorted(dicts, key=itemgetter(SORT_KEY))
if __name__ == '__main__':
    sample_dicts = [{'name': 'Alice', 'value': 25}, {'name': 'Bob', 'value': 30}, {'name': 'Charlie', 'value': 20}]
    sorted_dicts = sort_dicts_by_key(sample_dicts)
    print(sorted_dicts)