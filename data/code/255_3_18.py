class TupleSumFinder:
    @staticmethod
    def find_max_sum_tuple(tuples_list):
        if not tuples_list:
            return None
        return max(tuples_list, key=sum)

if __name__ == '__main__':
    sample_data = [(10, 5, 22, 8), (30, 15, 40, 25), (1, 50, 3)]
    max_tuple = TupleSumFinder.find_max_sum_tuple(sample_data)
    print(max_tuple)