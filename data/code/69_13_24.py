class ListElementFetcher:
    EMPTY_TUPLE = ()

    @staticmethod
    def get_first_last_middle_elements(numbers):
        if not numbers:
            return ListElementFetcher.EMPTY_TUPLE
        first = numbers[0]
        last = numbers[-1]
        middle_index = len(numbers) // 2
        middle = numbers[middle_index]
        return (first, last, middle)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = ListElementFetcher.get_first_last_middle_elements(sample_list)
    print(result)