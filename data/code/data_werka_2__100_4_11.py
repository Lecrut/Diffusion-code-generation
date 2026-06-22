class IntegerComparator:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def is_first_greater(self) -> bool:
        return self.x > self.y

    def is_second_greater(self) -> bool:
        return self.y > self.x

    def are_equal(self) -> bool:
        return self.x == self.y

if __name__ == '__main__':
    comparator = IntegerComparator(10, 5)
    print(comparator.is_first_greater())
    print(comparator.is_second_greater())
    print(comparator.are_equal())