class MinFinder:
    @staticmethod
    def find_min(lst):
        if not lst:
            raise ValueError("List cannot be empty")
        minimum = lst[0]
        for element in lst[1:]:
            if element < minimum:
                minimum = element
        return minimum

if __name__ == '__main__':
    sample_list = [4, 6, 2, 9, 3]
    min_value = MinFinder.find_min(sample_list)
    print(min_value)