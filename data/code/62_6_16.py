class SafeListAccessor:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    sample_list_a = [100, 200, 300]
    sample_list_b = [400]
    sample_list_c = []

    accessor_a = SafeListAccessor(sample_list_a)
    accessor_b = SafeListAccessor(sample_list_b)
    accessor_c = SafeListAccessor(sample_list_c)

    print(f"Second element of {sample_list_a}: {accessor_a.get_second_element()}")
    print(f"Second element of {sample_list_b}: {accessor_b.get_second_element()}")
    print(f"Second element of {sample_list_c}: {accessor_c.get_second_element()}")