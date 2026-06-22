class ObjectSorter:
    def __init__(self, objects):
        self.objects = objects

    def sort_by_key(self, key):
        return sorted(self.objects, key=lambda x: x.get(key))

if __name__ == '__main__':
    sample_data = [
        {'fruit': 'Apple', 'quantity': 50},
        {'fruit': 'Banana', 'quantity': 30},
        {'fruit': 'Cherry', 'quantity': 20}
    ]
    sorter = ObjectSorter(sample_data)
    sorted_by_quantity = sorter.sort_by_key('quantity')
    print("Sorted by quantity:", sorted_by_quantity)

    sorted_by_fruit = sorter.sort_by_key('fruit')
    print("Sorted by fruit:", sorted_by_fruit)