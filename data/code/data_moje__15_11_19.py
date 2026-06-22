def fetch_second_to_last(data):
    if len(data) < 2:
        raise IndexError("Sequence too short to retrieve penultimate item")
    return data[-2]

class SequenceAccessor:
    def __init__(self, items):
        self.items = items

    def get_penultimate_value(self):
        return fetch_second_to_last(self.items)

if __name__ == '__main__':
    test_data = [100, 200, 300, 400]
    accessor = SequenceAccessor(test_data)
    print(accessor.get_penultimate_value())
    try:
        fetch_second_to_last([99])
    except IndexError as err:
        print(err)