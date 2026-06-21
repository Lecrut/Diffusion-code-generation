class ArrayUtils:
    def __init__(self, array):
        if not isinstance(array, list):
            raise TypeError("Input must be a list")
        self.array = array

    def get_final_item(self):
        if len(self.array) == 0:
            raise ValueError("List cannot be empty")
        return self.array[-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    utils = ArrayUtils(sample_list)
    print(utils.get_final_item())

    another_list = ['a', 'b', 'c']
    another_utils = ArrayUtils(another_list)
    print(another_utils.get_final_item())

    empty_list = []
    try:
        empty_utils = ArrayUtils(empty_list)
        print(empty_utils.get_final_item())
    except ValueError as e:
        print(e)

    single_element_list = [42]
    single_utils = ArrayUtils(single_element_list)
    print(single_utils.get_final_item())