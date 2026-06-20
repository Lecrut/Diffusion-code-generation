class LogicSequence:
    def __init__(self):
        self.bool_list1 = [True, False, True]
        self.bool_list2 = [False, True, False]

    def generate_sequence(self):
        for b1, b2 in zip(self.bool_list1, self.bool_list2):
            yield b1 and b2

if __name__ == '__main__':
    logic_seq_instance = LogicSequence()
    print(next(logic_seq_instance.generate_sequence()))
    print(next(logic_seq_instance.generate_sequence()))
    print(next(logic_seq_instance.generate_sequence()))