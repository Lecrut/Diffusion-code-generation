class SafeListWrapper:
    def __init__(self, data):
        self._data = data

    def _has_second_element(self):
        return len(self._data) > 1

    def get_second_element_safe(self):
        if not self._has_second_element():
            return "IndexError: List does not have a second element"
        try:
            return self._data[1]
        except IndexError as e:
            return f"IndexError: {str(e)}"

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40]
    sample_list_b = [5]
    sample_list_c = []
    wrapper_a = SafeListWrapper(sample_list_a)
    wrapper_b = SafeListWrapper(sample_list_b)
    wrapper_c = SafeListWrapper(sample_list_c)
    print(f"Result for {sample_list_a}: {wrapper_a.get_second_element_safe()}")
    print(f"Result for {sample_list_b}: {wrapper_b.get_second_element_safe()}")
    print(f"Result for {sample_list_c}: {wrapper_c.get_second_element_safe()}")