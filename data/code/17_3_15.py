def _validate_nonempty(collection):
    if not collection:
        raise IndexError("cannot retrieve last element from an empty collection")

def _get_length(collection):
    return len(collection)

def get_last_element(collection):
    _validate_nonempty(collection)
    return collection[_get_length(collection) - 1]

class LastElementRetriever:
    def __init__(self, items):
        self._items = items

    def retrieve(self):
        return get_last_element(self._items)

if __name__ == '__main__':
    numbers = [100, 200, 300, 400, 500]
    chars = ('x', 'y', 'z')
    text = "final"
    
    print(get_last_element(numbers))
    print(get_last_element(chars))
    print(get_last_element(text))
    
    retriever = LastElementRetriever([7, 8, 9])
    print(retriever.retrieve())