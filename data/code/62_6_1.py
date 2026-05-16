class SafeListWrapper:
    def __init__(self, data):
        self._data = data
    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError:
            return "IndexError: List does not have a second element"
if __name__ == '__main__':
    sample_list_one = [10, 20, 30, 40]
    sample_list_two = [5]
    sample_list_empty = []
    wrapper_one = SafeListWrapper(sample_list_one)
    wrapper_two = SafeListWrapper(sample_list_two)
    wrapper_empty = SafeListWrapper(sample_list_empty)
    print(f"Result for {sample_list_one}: {wrapper_one.get_second_element()}")
    print(f"Result for {sample_list_two}: {wrapper_two.get_second_element()}")
    print(f"Result for {sample_list_empty}: {wrapper_empty.get_second_element()}")