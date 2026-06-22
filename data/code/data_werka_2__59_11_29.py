class ListUtils:
    @staticmethod
    def find_middle_item(numbers):
        if not numbers:
            raise ValueError("The list is empty")
        index = len(numbers) // 2
        return numbers[index]

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    middle_element = ListUtils.find_middle_item(sample_data)
    print(middle_element)