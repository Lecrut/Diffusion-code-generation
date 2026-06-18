class SetCounter:
    def __init__(self, data):
        self._set = set(data)
    def count(self):
        return len(self._set)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 1, 5]
    counter = SetCounter(sample_list)
    total_count = counter.count()
    print(total_count)