class StringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0

    def has_next(self):
        return self.index < len(self.string)

    def next_char(self):
        if self.has_next():
            char = self.string[self.index]
            self.index += 1
            return char
        else:
            raise StopIteration("No more characters")

if __name__ == '__main__':
    iterator = StringIterator('Python')
    while iterator.has_next():
        print(iterator.next_char())