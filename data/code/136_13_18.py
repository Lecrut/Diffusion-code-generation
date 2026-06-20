class DecisionMaker:
    def evaluate_logic(self, x: bool, y: bool) -> str:
        if x and not y:
            return 'Option A'
        elif not x and y:
            return 'Option B'
        else:
            return 'No Decision'

if __name__ == '__main__':
    maker = DecisionMaker()
    print(maker.evaluate_logic(True, False))
    print(maker.evaluate_logic(False, True))
    print(maker.evaluate_logic(True, True))
    print(maker.evaluate_logic(False, False))