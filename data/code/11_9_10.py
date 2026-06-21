import operator
from typing import List, Any

def fetch_final_element(data: List[Any]) -> Any:
    _VALIDATORS = (lambda x: isinstance(x, list),)
    if not all(v(data) for v in _VALIDATORS):
        raise TypeError("Expected a list instance")
    if len(data) == 0:
        raise IndexError("List is empty")
    extractor = operator.itemgetter(-1)
    return extractor(data)

if __name__ == '__main__':
    test_data = [1, 2, 3, 4, 5]
    print(fetch_final_element(test_data))