def get_last_element(iterable):
    try:
        iterator = iter(iterable)
        last_item = None
        while True:
            item = next(iterator)
            last_item = item
        return last_item
    except StopIteration:
        pass
class LastElementRetriever:
    def __init__(self, iterable):
        self._iterable = list(iterable) if hasattr(iterable, '__len__') else []
    def get_last(self):
        if not self._iterable:
            return None
        return self._iterable[-1]
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = (1, 'a', True)
    empty_list = []
    result_list = get_last_element(sample_list)
    print(f"List last: {result_list}")
    retriever = LastElementRetriever(sample_tuple)
    print(f"Tuple last via class: {retriever.get_last()}")
    try:
        empty_result = get_last_element(empty_list)
        print(f"Empty list result: {empty_result}")
    except Exception as e:
        print(f"Exception occurred: {e}")