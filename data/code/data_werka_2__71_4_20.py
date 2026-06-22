class ListProcessor:
    EMPTY_LIST_ERROR = "List must contain at least one element."

    @staticmethod
    def get_middle_element(numbers):
        if not numbers:
            raise ValueError(ListProcessor.EMPTY_LIST_ERROR)
        length = len(numbers)
        index = (length - 1) // 2
        return numbers[index]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = ListProcessor.get_middle_element(sample_numbers)
    print(result)