import bisect

class ListCentralValueFinder:
    @staticmethod
    def get_central_value(sorted_list):
        n = len(sorted_list)
        if n == 0:
            raise ValueError("Cannot find the middle of an empty list")
        return sorted_list[n // 2]

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    print(f"Central value of {sample_list1}: {ListCentralValueFinder.get_central_value(sample_list1)}")
    sample_list2 = [10, 20, 30, 40, 50, 60]
    print(f"Central value of {sample_list2}: {ListCentralValueFinder.get_central_value(sample_list2)}")
    sample_list3 = [1, 2, 3, 4]
    try:
        print(f"Central value of {sample_list3}: {ListCentralValueFinder.get_central_value(sample_list3)}")
    except ValueError as e:
        print(e)