class MaxFinder:
    def find_max(self, values):
        if not values:
            return None
        maximum = max(values)
        return maximum

if __name__ == '__main__':
    finder = MaxFinder()
    list1 = [10, 5, 20, 8, 15]
    tuple2 = (3, -1, 99, 42)
    empty_list = []
    print(f"Maximum of {list1}: {finder.find_max(list1)}")
    print(f"Maximum of {tuple2}: {finder.find_max(tuple2)}")
    print(f"Maximum of an empty list: {finder.find_max(empty_list)}")