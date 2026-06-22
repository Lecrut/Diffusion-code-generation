class HollowSquare:
    def __init__(self, size, delimiter='*'):
        if size <= 0:
            raise ValueError("Size must be positive")
        self.size = size
        self.delimiter = delimiter

    def build(self):
        size = self.size
        delim = self.delimiter
        if size == 1:
            return [delim]
        first_last = [delim * size]
        middle = [delim + ' ' * (size - 2) + delim] * (size - 2) if size > 2 else []
        return first_last + middle + first_last

    def build_generator(self):
        size = self.size
        delim = self.delim
        if size <= 0:
            return
        if size == 1:
            yield delim
            return
        top = delim * size
        yield top
        middle_len = size - 2
        if middle_len > 0:
            mid_part = delim + ' ' * middle_len + delim
            yield from (mid_part for _ in range(middle_len))
        yield top

if __name__ == '__main__':
    square = HollowSquare(5)
    result = square.build()
    for line in result:
        print(line)
    print("---")
    gen = list(HollowSquare(5).build_generator())
    for line in gen:
        print(line)