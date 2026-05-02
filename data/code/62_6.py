class CustomListWrapper:
    def __init__(self, data):
        self._data = data
    def get_second_element_safe(self):
        try:
            return self._data[1]
        except IndexError:
            return "IndexError: List does not have a second element"
if __name__ == '__main__':
    sample_list_1 = [10, 20, 30, 40]
    sample_list_2 = [5]
    sample_list_3 = []
    wrapper1 = CustomListWrapper(sample_list_1)
    wrapper2 = CustomListWrapper(sample_list_2)
    wrapper3 = CustomListWrapper(sample_list_3)
    print(f"Wrapper 1 result: {wrapper1.get_second_element_safe()}")
    print(f"Wrapper 2 result: {wrapper2.get_second_element_safe()}")
    print(f"Wrapper 3 result: {wrapper3.get_second_element_safe()}")