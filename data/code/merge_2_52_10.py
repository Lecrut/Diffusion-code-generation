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
        self.iterable = list(iterable) if not isinstance(iterable, (list, tuple)) else iter(list(iterable))
    def get_last(self):
        try:
            iterator = iter(self.iterable)
            last_item = None
            while True:
                item = next(iterator)
                last_item = item
            return last_item
        except StopIteration:
            pass
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    empty_list = []
    retriever = LastElementRetriever(sample_list)
    result = retriever.get_last()
    if result is not None:
        print(f"Last element of {sample_list}: {result}")
    else:
        print("List was empty.")