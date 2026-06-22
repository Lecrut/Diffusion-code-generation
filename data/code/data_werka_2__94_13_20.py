from typing import Callable, Iterable, Any

def any_matches(iterable: Iterable[Any], predicate: Callable[[Any], bool]) -> bool:
    result = False
    for element in iterable:
        if predicate(element):
            result = True
            break
    return result

if __name__ == '__main__':
    data = (10, 20, 30, 40, 50)
    check = any_matches(data, lambda val: val > 25)
    print(check)