def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

class Searcher:
    def search(self, data, value):
        result = binary_search(data, value)
        if result != -1:
            print(f"Value {value} found at index {result}")
        else:
            print(f"Value {value} not found in the list")

if __name__ == '__main__':
    searcher = Searcher()
    data_list = [1, 3, 5, 7, 9, 11, 13]
    search_value = 7
    searcher.search(data_list, search_value)
    
    search_value = 8
    searcher.search(data_list, search_value)