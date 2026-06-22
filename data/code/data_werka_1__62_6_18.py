class SafeListAccess:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError:
            return "IndexError: List does not have a second element"

if __name__ == '__main__':
    sample_data_1 = [100, 200, 300, 400]
    sample_data_2 = ['a', 'b']
    sample_data_3 = []
    
    access_wrapper_1 = SafeListAccess(sample_data_1)
    access_wrapper_2 = SafeListAccess(sample_data_2)
    access_wrapper_3 = SafeListAccess(sample_data_3)

    print(f"Second element of {sample_data_1}: {access_wrapper_1.get_second_element()}")
    print(f"Second element of {sample_data_2}: {access_wrapper_2.get_second_element()}")
    print(f"Second element of {sample_data_3}: {access_wrapper_3.get_second_element()}")