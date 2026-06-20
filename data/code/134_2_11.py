class ExclusiveConditionChecker:
    def __init__(self, condition1: bool, condition2: bool, condition3: bool, condition4: bool):
        self.conditions = [condition1, condition2, condition3, condition4]

    def is_exclusive(self) -> bool:
        return (self.conditions[0] ^ self.conditions[1]) or \
               (self.conditions[0] ^ self.conditions[2]) or \
               (self.conditions[0] ^ self.conditions[3]) or \
               (self.conditions[1] ^ self.conditions[2]) or \
               (self.conditions[1] ^ self.conditions[3]) or \
               (self.conditions[2] ^ self.conditions[3])

if __name__ == '__main__':
    checker = ExclusiveConditionChecker(True, False, True, False)
    print(checker.is_exclusive())