class LargestElementChecker:
    def __init__(self, lst):
        if not lst:
            raise ValueError("The list cannot be empty")
        self.lst = lst

    @staticmethod
    def find_max_recursive(lst, index):
        if index == 0:
            return lst[0]
        else:
            current_max = LargestElementChecker.find_max_recursive(lst, index - 1)
            return max(current_max, lst[index])

    def is_largest_greater_than_target(self, target):
        largest_element = LargestElementChecker.find_max_recursive(self.lst, len(self.lst) - 1)
        return largest_element > target

if __name__ == '__main__':
    sample_list = [15, 25, 35, 45, 55]
    target_value = 30
    checker = LargestElementChecker(sample_list)
    result = checker.is_largest_greater_than_target(target_value)
    print(result)