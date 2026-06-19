class SafeListAccess:
    def __init__(self, data):
        self._data = data

    def get_second_element(self):
        try:
            return self._data[1]
        except IndexError as e:
            return f"Error: {str(e)}"

if __name__ == '__main__':
    SAMPLE_LIST_A = [10, 20, 30, 40]
    SAMPLE_LIST_B = [5]
    SAMPLE_LIST_C = []

    wrapper_a = SafeListAccess(SAMPLE_LIST_A)
    wrapper_b = SafeListAccess(SAMPLE_LIST_B)
    wrapper_c = SafeListAccess(SAMPLE_LIST_C)

    print(f"Result for {SAMPLE_LIST_A}: {wrapper_a.get_second_element()}")
    print(f"Result for {SAMPLE_LIST_B}: {wrapper_b.get_second_element()}")
    print(f"Result for {SAMPLE_LIST_C}: {wrapper_c.get_second_element()}")