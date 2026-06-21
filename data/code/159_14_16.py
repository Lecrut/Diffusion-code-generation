class NumberFilter:
    def extract_odds(self, numbers: list[int]) -> list[int]:
        return [num for num in numbers if num % 2 != 0]

if __name__ == '__main__':
    filter_instance = NumberFilter()
    sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_instance.extract_odds(sample_list)
    print(odd_numbers)