class ListWrapper:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    sample_list_a = [100, 200, 300, 400]
    sample_list_b = [500]
    sample_list_c = []
    
    wrapper_a = ListWrapper(sample_list_a)
    wrapper_b = ListWrapper(sample_list_b)
    wrapper_c = ListWrapper(sample_list_c)

    print(f"Second element of {sample_list_a}: {wrapper_a.get_second_element()}")
    print(f"Second element of {sample_list_b}: {wrapper_b.get_second_element()}")
    print(f"Second element of {sample_list_c}: {wrapper_c.get_second_element()}")