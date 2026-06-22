class TupleSumFinder:
    @staticmethod
    def find_max_sum_tuple(data_list):
        if not data_list:
            return None
        return max(data_list, key=sum)

if __name__ == '__main__':
    sample_data = [(10, 5), (30, 15), (40, 25)]
    max_tuple = TupleSumFinder.find_max_sum_tuple(sample_data)
    print(max_tuple)