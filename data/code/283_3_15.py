class ListChecker:
    def is_sorted_ascending(self, data_list):
        return all(data_list[i] <= data_list[i + 1] for i in range(len(data_list) - 1))

if __name__ == '__main__':
    checker = ListChecker()
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data}")
    print(f"Is Sorted Ascending: {checker.is_sorted_ascending(sample_data)}")
    
    sample_data_desc = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"Data: {sample_data_desc}")
    print(f"Is Sorted Ascending: {checker.is_sorted_ascending(sample_data_desc)}")
    
    sample_data_mixed = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    print(f"Data: {sample_data_mixed}")
    print(f"Is Sorted Ascending: {checker.is_sorted_ascending(sample_data_mixed)}")