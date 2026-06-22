class ListChecker:
    @staticmethod
    def is_sorted_ascending(numbers):
        return all(numbers[i+1] > numbers[i] for i in range(len(numbers) - 1))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    output = ListChecker.is_sorted_ascending(sample_list)
    print(output)