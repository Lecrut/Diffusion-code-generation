class LogicGenerator:
    def __init__(self):
        self.bool_list1 = [True, False, True]
        self.bool_list2 = [False, True, False]

    def logic_sequence(self):
        for b1, b2 in zip(self.bool_list1, self.bool_list2):
            yield b1 and b2

if __name__ == '__main__':
    generator = LogicGenerator()
    print(next(generator.logic_sequence()))
    print(next(generator.logic_sequence()))
    print(next(generator.logic_sequence()))