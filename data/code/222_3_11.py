class MinFinder:
    @staticmethod
    def find_min(lst):
        return min(lst, key=lambda x: x)

if __name__ == '__main__':
    sample_list = [8, 3, 5, 7, 2]
    min_value = MinFinder.find_min(sample_list)
    print(min_value)