class MaxFinder:
    @staticmethod
    def find_max(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        return max(data)

if __name__ == '__main__':
    sample_list1 = [10, 5, 20, 8, 15]
    sample_list2 = [-5, -1, -10, -3]
    sample_list3 = [42]
    print(f"The largest value in {sample_list1} is: {MaxFinder.find_max(sample_list1)}")
    print(f"The largest value in {sample_list2} is: {MaxFinder.find_max(sample_list2)}")
    print(f"The largest value in {sample_list3} is: {MaxFinder.find_max(sample_list3)}")