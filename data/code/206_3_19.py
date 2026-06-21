class MinFinder:
    @staticmethod
    def find_min(lst):
        if not lst:
            raise ValueError('List is empty')
        min_item = lst[0]
        for item in lst[1:]:
            if item < min_item:
                min_item = item
        return min_item

if __name__ == '__main__':
    sample_list = [4, 2, 9, 6, 3]
    minimum_value = MinFinder.find_min(sample_list)
    print(minimum_value)