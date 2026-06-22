class TupleAverager:
    def __init__(self, tuples):
        self.tuples = tuples

    def sum_of_elements(self):
        return sum(sum(t) for t in self.tuples)

    def total_element_count(self):
        return sum(len(t) for t in self.tuples)

    def average(self):
        count = self.total_element_count()
        if count == 0:
            return 0
        total_sum = self.sum_of_elements()
        return total_sum / count

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5, 6))
    averager = TupleAverager(sample_data)
    print("Sum of elements:", averager.sum_of_elements())
    print("Total element count:", averager.total_element_count())
    print("Average:", averager.average())