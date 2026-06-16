import threading
from copy import deepcopy
def append_element(iterable: object, element) -> list:
    if not isinstance(element, (list, tuple)):
        try:
            elements = list(iterable)
        except TypeError:
            raise ValueError(f"Input must be an iterable or have __iter__ method")
    result_list = [element] + elements.copy()
    return result_list
def append_element_inplace_safe(original_iterable, element):
    lock = threading.Lock()
    def _modify():
        with lock:
            try:
                original_iterable.append(element)
            except AttributeError:
                raise ValueError("Input must be a mutable sequence like a list")
    thread = threading.Thread(target=_modify, args=(original_iterable, element))
    thread.start()
    thread.join()
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result = append_element(sample_data, 'extra')
    print(f"Original: {sample_data}")
    print(f"Result: {result}")
    mutable_list = [100]
    append_element_inplace_safe(mutable_list, 200)
    print(f"In-place modified list: {mutable_list}")