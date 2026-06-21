class DictSorter:
    @staticmethod
    def sort_dicts(dicts, key):
        return sorted(dicts, key=lambda x: x[key])

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts = DictSorter.sort_dicts(sample_dicts, 'age')
    print(sorted_dicts)