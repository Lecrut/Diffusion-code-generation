class ListChecker:
    def is_sorted(self, data_list):
        return all(data_list[i] <= data_list[i + 1] for i in range(len(data_list) - 1))

if __name__ == '__main__':
    checker = ListChecker()
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result_sorted = checker.is_sorted(sample_data)
    print(f"Data: {sample_data}")
    print(f"Is Sorted: {result_sorted}")

    sample_data_descending = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    result_not_sorted = checker.is_sorted(sample_data_descending)
    print(f"Data: {sample_data_descending}")
    print(f"Is Sorted: {result_not_sorted}")