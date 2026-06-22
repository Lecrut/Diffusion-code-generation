class TupleFilter:
    def filter_even_tuples(self, tuples):
        return [t for t in tuples if t[1] % 2 == 0]

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    filter_instance = TupleFilter()
    result = filter_instance.filter_even_tuples(sample_data)
    print(result)