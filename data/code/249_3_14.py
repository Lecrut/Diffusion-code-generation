class MaxFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [-10, -5, -20]
    list3 = [42]
    empty_list = []
    print(f"Largest in {list1}: {MaxFinder.find_largest(list1)}")
    print(f"Largest in {list2}: {MaxFinder.find_largest(list2)}")
    print(f"Largest in {list3}: {MaxFinder.find_largest(list3)}")
    try:
        MaxFinder.find_largest(empty_list)
    except ValueError as e:
        print(e)