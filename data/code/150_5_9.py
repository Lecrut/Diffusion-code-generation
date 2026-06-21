class Deduplicator:
    def __init__(self, data):
        self.data = data

    def remove_duplicates(self, item_to_remove):
        return [item for item in self.data if item != item_to_remove]

if __name__ == '__main__':
    deduplicator_instance = Deduplicator([1, 2, 3, 4, 5, 2, 3])
    result = deduplicator_instance.remove_duplicates(3)
    print(result)