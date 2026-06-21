class ValueCounter:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def count_occurrences(lst, target):
        return lst.count(target)

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5, 2, 2, 3]
    target_value = 2
    counter = ValueCounter(sample_data)
    count = counter.count_occurrences(counter.data, target_value)
    print(count)