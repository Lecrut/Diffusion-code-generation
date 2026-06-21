class ObjectSorter:
    @staticmethod
    def sort_by_key(objects, key):
        if not all(isinstance(obj, dict) for obj in objects):
            raise ValueError("All elements must be dictionaries.")
        return sorted(objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'title': 'Fiction', 'year': 1995},
        {'title': 'Non-Fiction', 'year': 2005},
        {'title': 'Science', 'year': 1985}
    ]
    sorted_data = ObjectSorter.sort_by_key(sample_data, 'year')
    print(sorted_data)