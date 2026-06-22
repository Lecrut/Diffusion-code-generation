class SafeListAccess:

    def __init__(self, data):
        self.data = data

    def get_last_element(self):
        try:
            return self.data[-1]
        except IndexError:
            return None
if __name__ == '__main__':
    sample_data_1 = [1, 2, 3, 4, 5]
    sample_data_2 = []
    sample_data_3 = ['a', 'b', 'c']
    safe_access_1 = SafeListAccess(sample_data_1)
    safe_access_2 = SafeListAccess(sample_data_2)
    safe_access_3 = SafeListAccess(sample_data_3)
    print(safe_access_1.get_last_element())
    print(safe_access_2.get_last_element())
    print(safe_access_3.get_last_element())