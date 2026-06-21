DEFAULT_EMPTY_RESULT = None

def _is_empty(item_list):
    return len(item_list) == 0

def _get_tail(item_list):
    return item_list[-1]

class SequenceHolder:
    def __init__(self):
        self._data = []

    def add(self, value):
        self._data.append(value)

    def retrieve_final(self):
        if _is_empty(self._data):
            return DEFAULT_EMPTY_RESULT
        return _get_tail(self._data)

if __name__ == '__main__':
    holder = SequenceHolder()
    holder.add(100)
    holder.add(200)
    holder.add(300)
    result = holder.retrieve_final()
    print(result)