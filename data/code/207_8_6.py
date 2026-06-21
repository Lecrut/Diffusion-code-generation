class MaxFinder:
    @staticmethod
    def find_max_element(sorted_list):
        return sorted_list[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    max_finder = MaxFinder()
    print(max_finder.find_max_element(sample_list))