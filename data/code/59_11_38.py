class ListUtils:
    EMPTY_LIST_ERROR = "The list is empty"

    @staticmethod
    def find_middle_item(numbers):
        if not numbers:
            raise ValueError(ListUtils.EMPTY_LIST_ERROR)
        index = len(numbers) // 2
        return numbers[index]

if __name__ == '__main__':
    sample_list = [5, 15, 25, 35, 45]
    middle_item = ListUtils.find_middle_item(sample_list)
    print(middle_item)