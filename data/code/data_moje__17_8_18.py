import collections.abc

class SequenceAccessor:
    def __init__(self, target):
        if not isinstance(target, collections.abc.Sequence):
            raise TypeError("Target must be a sequence")
        if len(target) == 0:
            raise ValueError("Sequence cannot be empty")
        self._target = target

    def get_last(self):
        return self._target[-1]

    def get_first(self):
        return self._target[0]

    def get_length(self):
        return len(self._target)

def process_list(items):
    accessor = SequenceAccessor(items)
    return accessor.get_last()

if __name__ == '__main__':
    data = [7, 14, 21, 28, 35]
    obj = SequenceAccessor(data)
    print(obj.get_last())
    print(obj.get_first())
    print(obj.get_length())
    print(process_list(data))