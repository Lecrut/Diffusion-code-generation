class MaxElementFinder:
    @staticmethod
    def find_max_element(sorted_list):
        return sorted_list[-1]

if __name__ == '__main__':
    sample_list = [3, 5, 7, 9]
    max_element = MaxElementFinder.find_max_element(sample_list)
    print(max_element)