class BooleanLogicProcessor:
    def __init__(self):
        self.logic_map = {True: False, False: True}

    def get_negation(self, flag: bool) -> bool:
        if flag in self.logic_map:
            return self.logic_map[flag]
        raise ValueError(f"Unsupported boolean value: {flag}")

if __name__ == '__main__':
    processor = BooleanLogicProcessor()
    true_result = processor.get_negation(True)
    false_result = processor.get_negation(False)
    print(true_result)
    print(false_result)