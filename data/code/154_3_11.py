class ValueCounter:
    def __init__(self, data):
        self.data = data

    def count_occurrences(self, target):
        return self.data.count(target)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 2, 3]
    counter = ValueCounter(sample_list)
    print(counter.count_occurrences(2))
    print(counter.count_occurrences(3))