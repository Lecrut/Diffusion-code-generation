class ListUtils:
    @staticmethod
    def find_middle_element(data):
        n = len(data)
        middle_index = (n - 1) // 2
        return data[middle_index]

if __name__ == '__main__':
    sample_lists = [
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [100],
        [5, 15, 25, 35, 45, 55]
    ]
    for lst in sample_lists:
        print(f"Middle element of {lst}: {ListUtils.find_middle_element(lst)}")