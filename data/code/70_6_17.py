class ElementAccessor:
    def __init__(self, data):
        self.data = data

    def first_and_last(self):
        if len(self.data) < 2:
            raise ValueError("List must contain at least two elements.")
        return (self.data[0], self.data[-1])

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    accessor = ElementAccessor(sample_list)
    try:
        result = accessor.first_and_last()
        print(f"First and last of list: {result}")
    except ValueError as e:
        print(f"Error: {e}")