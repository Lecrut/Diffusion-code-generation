class DictMerger:
    def __init__(self):
        self.result = {}

    def merge_pairs(self, pairs):
        for key, value in pairs:
            self.result[key] = value

    def get_result(self):
        return self.result

if __name__ == '__main__':
    merger = DictMerger()
    sample_data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    merger.merge_pairs(sample_data)
    print(merger.get_result())