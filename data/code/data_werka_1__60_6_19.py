class SafeListAccess:
    def __init__(self, data):
        self.data = data

    def get_last_element(self):
        if not isinstance(self.data, list):
            raise TypeError("Input must be a list.")
        if len(self.data) == 0:
            raise ValueError("The list is empty.")
        return self.data[-1]

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    safe_access = SafeListAccess(sample_data)
    try:
        print(safe_access.get_last_element())
    except (TypeError, ValueError) as e:
        print(e)

    empty_list = []
    safe_access_empty = SafeListAccess(empty_list)
    try:
        print(safe_access_empty.get_last_element())
    except (TypeError, ValueError) as e:
        print(e)