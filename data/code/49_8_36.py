class LengthComparator:

    def __init__(self, length1, length2):
        self.length1 = length1
        self.length2 = length2

    def get_min_length(self):
        return min(self.length1, self.length2)

    def get_max_length(self):
        return max(self.length1, self.length2)

def compare_lengths(length1, length2):
    comparator = LengthComparator(length1, length2)
    return (comparator.get_min_length(), comparator.get_max_length())
if __name__ == '__main__':
    sample_length1 = 50
    sample_length2 = 30
    result = compare_lengths(sample_length1, sample_length2)
    print(result)
    another_comparator = LengthComparator(40, 60)
    print('Min length:', another_comparator.get_min_length())
    print('Max length:', another_comparator.get_max_length())