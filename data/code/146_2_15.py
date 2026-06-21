class DictSorter:
    @staticmethod
    def sort_by_key(dicts, key):
        return sorted(dicts, key=lambda d: d.get(key))

if __name__ == '__main__':
    sample_dicts = [
        {'name': 'Alice', 'age': 25},
        {'name': 'Bob', 'age': 30},
        {'name': 'Charlie', 'age': 20}
    ]
    sorted_dicts_age = DictSorter.sort_by_key(sample_dicts, 'age')
    print(sorted_dicts_age)