class TupleFilter:
    @staticmethod
    def filter_even_tuples(tuples_list):
        return [t for t in tuples_list if t[1] % 2 == 0]

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    filtered_data = TupleFilter.filter_even_tuples(sample_data)
    print(filtered_data)