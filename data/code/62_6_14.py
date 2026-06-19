class SafeListAccess:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError as e:
            return str(e)

if __name__ == '__main__':
    test_list_1 = [7, 8, 9]
    test_list_2 = ['a']
    test_list_3 = []
    
    wrapper_1 = SafeListAccess(test_list_1)
    wrapper_2 = SafeListAccess(test_list_2)
    wrapper_3 = SafeListAccess(test_list_3)

    result_1 = wrapper_1.get_second_element()
    result_2 = wrapper_2.get_second_element()
    result_3 = wrapper_3.get_second_element()

    print(f"Result for test_list_1: {result_1}")
    print(f"Result for test_list_2: {result_2}")
    print(f"Result for test_list_3: {result_3}")