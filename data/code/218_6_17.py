class MinFinder:
    def __init__(self, data):
        self.data = data

    def find_minimum(self):
        if not self.data:
            return None
        current_min = self.data[0]
        for element in self.data[1:]:
            if element < current_min:
                current_min = element
        return current_min

if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9, 3]
    min_finder = MinFinder(sample_list)
    result = min_finder.find_minimum()
    print(result)
    
    sample_list_2 = [42, 10, 55, 3, 88]
    min_finder_2 = MinFinder(sample_list_2)
    result_2 = min_finder_2.find_minimum()
    print(result_2)