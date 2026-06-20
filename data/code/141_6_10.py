class BooleanFlags:

    def __init__(self):
        self.flags = [0, 0]

    def set_flag(self, index: int, value: bool) -> None:
        self.flags[index] = int(value)

    def get_and_result(self) -> int:
        return self.flags[0] & self.flags[1]

    def get_or_result(self) -> int:
        return self.flags[0] | self.flags[1]

    def get_not_first_flag(self) -> int:
        return ~self.flags[0]
if __name__ == '__main__':
    bf = BooleanFlags()
    bf.set_flag(0, True)
    bf.set_flag(1, False)
    print(f'AND: {bf.get_and_result()}, OR: {bf.get_or_result()}, NOT (first flag): {bf.get_not_first_flag()}')