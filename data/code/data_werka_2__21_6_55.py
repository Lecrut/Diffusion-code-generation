def sort_objects_by_key(objects, key):
    if not all(isinstance(obj, dict) for obj in objects):
        raise ValueError("All elements must be dictionaries.")
    if not isinstance(key, str):
        raise ValueError("Key must be a string.")
    return sorted(objects, key=lambda x: x.get(key))

class Sorter:
    def __init__(self, data):
        self.data = data

    def sort_by_key(self, key):
        try:
            return sort_objects_by_key(self.data, key)
        except ValueError as e:
            print(f"Error during sorting: {e}")
            return []

if __name__ == '__main__':
    sample_data = [
        {'model': 'Tesla Model S', 'year': 2020},
        {'model': 'BMW X5', 'year': 2018},
        {'model': 'Audi A4', 'year': 2019}
    ]
    sorter = Sorter(sample_data)
    sorted_data = sorter.sort_by_key('year')
    print(sorted_data)