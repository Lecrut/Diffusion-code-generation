from operator import itemgetter

class DictSorter:
    @staticmethod
    def sort_by_key(data, key):
        return sorted(data, key=itemgetter(key))

if __name__ == '__main__':
    sample_list = [
        {'name': 'A', 'value': 30},
        {'name': 'B', 'value': 10},
        {'name': 'C', 'value': 20},
        {'name': 'D', 'value': 40}
    ]
    sorted_list = DictSorter.sort_by_key(sample_list, 'value')
    print(sorted_list)