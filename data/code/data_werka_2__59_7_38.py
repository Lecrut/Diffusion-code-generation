class ListProcessor:
    @staticmethod
    def find_middle_item(numbers):
        if not numbers:
            raise ValueError('The list cannot be empty')
        middle_index = len(numbers) // 2
        return numbers[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]
    print(ListProcessor.find_middle_item(sample_list_odd))
    print(ListProcessor.find_middle_item(sample_list_even))