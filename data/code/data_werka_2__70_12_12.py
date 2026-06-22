class ListAccessor:
    def __init__(self, data):
        self.data = data

    def get_boundaries(self):
        if not self.data:
            raise ValueError("List must not be empty")
        return self.data[0], self.data[-1]

    def get_first(self):
        return self.data[0]

    def get_last(self):
        return self.data[-1]

def process_list_access(data):
    accessor = ListAccessor(data)
    first = accessor.get_first()
    last = accessor.get_last()
    return first, last

if __name__ == '__main__':
    sample_values = [7, 14, 21, 28, 35]
    first_val, last_val = process_list_access(sample_values)
    print(first_val, last_val)