THIRD_INDEX = 2
MIN_LENGTH = 3

class ThirdItemRetriever:
    def __init__(self, data: list) -> None:
        if not isinstance(data, list):
            raise TypeError(f"Expected list, got {type(data).__name__}")
        self._data = data

    def retrieve(self) -> object:
        length = len(self._data)
        if length < MIN_LENGTH:
            raise IndexError(f"Need at least {MIN_LENGTH} items, found {length}")
        return self._data[THIRD_INDEX]

def get_third_item(lst: list) -> object:
    retriever = ThirdItemRetriever(lst)
    return retriever.retrieve()

if __name__ == '__main__':
    test_list = [100, 200, 300, 400]
    result = get_third_item(test_list)
    print(result)
    try:
        get_third_item([1, 2])
    except IndexError as exc:
        print(str(exc))
    try:
        get_third_item("string")
    except TypeError as exc:
        print(str(exc))