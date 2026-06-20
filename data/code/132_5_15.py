class LogicSequence:
    def __init__(self):
        self.bool_list1 = [True, False, True]
        self.bool_list2 = [False, True, False]

    def and_generator(self):
        for b1, b2 in zip(self.bool_list1, self.bool_list2):
            yield b1 and b2

if __name__ == '__main__':
    logic_seq = LogicSequence()
    gen = logic_seq.and_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))