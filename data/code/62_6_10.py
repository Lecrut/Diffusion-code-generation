class SafeListWrapper:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            second_element = self._data[1]
            return second_element
        except IndexError:
            error_message = "IndexError: List does not have a second element"
            return error_message

if __name__ == '__main__':
    sample_list_a = [10, 20, 30, 40]
    sample_list_b = [5]
    sample_list_c = []
    
    wrapper_a = SafeListWrapper(sample_list_a)
    wrapper_b = SafeListWrapper(sample_list_b)
    wrapper_c = SafeListWrapper(sample_list_c)

    print(f"Result for {sample_list_a}: {wrapper_a.get_second_element()}")
    print(f"Result for {sample_list_b}: {wrapper_b.get_second_element()}")
    print(f"Result for {sample_list_c}: {wrapper_c.get_second_element()}")