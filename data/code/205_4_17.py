from operator import itemgetter

class DictSorter:
    KEY = 'value'

    @staticmethod
    def sort_by_key(dicts):
        return sorted(dicts, key=itemgetter(DictSorter.KEY))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'A', 'value': 30},
        {'name': 'B', 'value': 10},
        {'name': 'C', 'value': 20},
        {'name': 'D', 'value': 40}
    ]
    sorted_dicts = DictSorter.sort_by_key(sample_dicts)
    print(sorted_dicts)