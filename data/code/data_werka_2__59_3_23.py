class MiddleElementFinder:
    @staticmethod
    def find_middle(lst):
        if len(lst) % 2 == 0:
            raise ValueError("List must have an odd length.")
        return lst[len(lst) // 2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(MiddleElementFinder.find_middle(sample_list))