class ListAccessor:

    def __init__(self, elements):
        self._elements = elements

    def get(self, index):
        if not isinstance(index, int):
            raise TypeError('Index must be an integer')
        try:
            return self._elements[index]
        except IndexError:
            raise IndexError('Position out of bounds')
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    accessor = ListAccessor(sample_list)
    try:
        print(accessor.get(2))
    except (IndexError, TypeError) as e:
        print(f'Error: {e}')
    try:
        print(accessor.get(5))
    except (IndexError, TypeError) as e:
        print(f'Error: {e}')
    try:
        print(accessor.get('two'))
    except (IndexError, TypeError) as e:
        print(f'Error: {e}')