def get_first_element(data):
    if not data:
        raise IndexError("list is empty")
    return data[0]

class ListProcessor:
    def __init__(self, data):
        self.data = data

    def first_element(self):
        return get_first_element(self.data)

if __name__ == '__main__':
    processor1 = ListProcessor([5, 6, 7, 8])
    processor2 = ListProcessor(['x', 'y', 'z'])
    empty_processor = ListProcessor([])

    try:
        print(f"First element of processor1: {processor1.first_element()}")
        print(f"First element of processor2: {processor2.first_element()}")
        empty_processor.first_element()
    except IndexError as e:
        print(f"Error caught: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")