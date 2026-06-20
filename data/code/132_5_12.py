class LogicSequenceGenerator:
    BOOL_LIST1 = [True, False, True]
    BOOL_LIST2 = [False, True, False]

    @staticmethod
    def and_operation(b1, b2):
        return b1 and b2

    def generate_logic_sequence(self):
        for b1, b2 in zip(self.BOOL_LIST1, self.BOOL_LIST2):
            yield self.and_operation(b1, b2)

if __name__ == '__main__':
    generator = LogicSequenceGenerator()
    print(list(generator.generate_logic_sequence()))