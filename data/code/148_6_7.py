class LargestValueFinder:
    @staticmethod
    def find_largest(data):
        if not data:
            raise ValueError("Cannot find the largest element in an empty list.")
        largest = data[0]
        for item in data[1:]:
            if item > largest:
                largest = item
        return largest

if __name__ == '__main__':
    finder = LargestValueFinder()
    sample_list1 = [1, 5, 2, 8, 3]
    sample_list2 = []
    sample_list3 = [-10, -5, -20]

    try:
        result1 = finder.find_largest(sample_list1)
        print(f"The largest element in {sample_list1} is: {result1}")
    except ValueError as e:
        print(f"Error for list1: {e}")

    try:
        result2 = finder.find_largest(sample_list2)
        print(f"The largest element in {sample_list2} is: {result2}")
    except ValueError as e:
        print(f"Error for list2: {e}")

    try:
        result3 = finder.find_largest(sample_list3)
        print(f"The largest element in {sample_list3} is: {result3}")
    except ValueError as e:
        print(f"Error for list3: {e}")