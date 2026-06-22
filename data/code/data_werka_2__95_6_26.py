class ConditionComposer:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def evaluate(self) -> bool:
        if self.a <= 0:
            return False
        if self.b % 2 != 0:
            return False
        if self.c % self.a != 0:
            return False
        return True

if __name__ == '__main__':
    composer = ConditionComposer(a=4, b=10, c=20)
    print(composer.evaluate())
    composer2 = ConditionComposer(a=3, b=9, c=27)
    print(composer2.evaluate())
    composer3 = ConditionComposer(a=-1, b=2, c=4)
    print(composer3.evaluate())