class SafeListWrapper:
    def __init__(self, data):
        self._data = data
    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError:
            return "IndexError: List does not have a second element"
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5]
    sample_list_3 = []
    wrapper1 = SafeListWrapper(sample_list_1)
    wrapper2 = SafeListWrapper(sample_list_2)
    wrapper3 = SafeListWrapper(sample_list_3)
    print(f"Result for {sample_list_1}: {wrapper1.get_second_element()}")
    print(f"Result for {sample_list_2}: {wrapper2.get_second_element()}")
    print(f"Result for {sample_list_3}: {wrapper3.get_second_element()}")