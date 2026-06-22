class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_bounds(self):
        if not self.data:
            raise ValueError("List cannot be empty")
        return self.data[0], self.data[-1]

def check_first_and_last(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    accessor = ListAccessor(lst)
    return accessor.get_bounds()

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    result = check_first_and_last(sample_list)
    print(result)
    accessor = ListAccessor([1, 2, 3])
    print(accessor.get_bounds())