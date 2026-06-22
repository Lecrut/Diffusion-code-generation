class MaxFinder:
    @staticmethod
    def find_max(lst):
        if not lst:
            raise ValueError("List is empty")
        max_elem = lst[0]
        for elem in lst[1:]:
            if elem > max_elem:
                max_elem = elem
        return max_elem

if __name__ == '__main__':
    sample_list = [7, 2, 9, 5, 3, 8]
    finder = MaxFinder()
    print(finder.find_max(sample_list))