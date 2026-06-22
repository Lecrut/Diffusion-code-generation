def get_first_element(data):
    try:
        return data[0]
    except (IndexError, TypeError) as error:
        raise ValueError("Input must be a non-empty sequence") from error

class ListAccessor:
    def __init__(self, values):
        self.values = values

    def fetch_head(self):
        return get_first_element(self.values)

if __name__ == '__main__':
    sample_data = [42, 17, 99, 3]
    accessor = ListAccessor(sample_data)
    print(accessor.fetch_head())