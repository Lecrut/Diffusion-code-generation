class NumberIterator:
    def __init__(self):
        self.current = 0

    def next_number(self):
        result = self.current
        self.current += 1
        return result

    def has_next(self):
        return self.current < 10

if __name__ == '__main__':
    iterator = NumberIterator()
    while iterator.has_next():
        print(iterator.next_number())