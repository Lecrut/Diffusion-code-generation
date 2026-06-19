class MiddleFinder:
    @staticmethod
    def find_middle_element(lst):
        if not isinstance(lst, list):
            raise TypeError("Input must be a list")
        if len(lst) == 0:
            raise ValueError("List cannot be empty")
        n = len(lst)
        middle_index = n // 2
        return lst[middle_index]

if __name__ == '__main__':
    sample_list = [7.1, 8.5, 9.3, 10.7, 11.2]
    print(MiddleFinder.find_middle_element(sample_list))