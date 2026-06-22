class SequenceEndChecker:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)

    def get_ends(self):
        if self.length == 0:
            return None
        if self.length == 1:
            return (self.sequence[0], self.sequence[0])
        return (self.sequence[0], self.sequence[-1])

    def is_empty(self):
        return self.length == 0

    def has_unique_ends(self):
        if self.length < 2:
            return False
        return self.sequence[0] != self.sequence[-1]

if __name__ == '__main__':
    list_instance = SequenceEndChecker([10, 20, 30])
    print(list_instance.get_ends())
    print(list_instance.is_empty())
    print(list_instance.has_unique_ends())

    str_instance = SequenceEndChecker("python")
    print(str_instance.get_ends())
    print(str_instance.has_unique_ends())

    empty_instance = SequenceEndChecker([])
    print(empty_instance.get_ends())
    print(empty_instance.is_empty())