from operator import itemgetter

class DictSorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        return sorted(self.data, key=itemgetter(key))

if __name__ == '__main__':
    sorter = DictSorter([
        {'name': 'A', 'value': 30},
        {'name': 'B', 'value': 10},
        {'name': 'C', 'value': 20},
        {'name': 'D', 'value': 40}
    ])
    sorted_data = sorter.sort_by_key('value')
    print(sorted_data)