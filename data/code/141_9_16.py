class LogicChain:

    def __init__(self, value):
        self.value = value

    def and_(self, other):
        return LogicChain(self.value and other.value)

    def or_(self, other):
        return LogicChain(self.value or other.value)

    def not_(self):
        return LogicChain(not self.value)
if __name__ == '__main__':
    p = LogicChain(True)
    q = LogicChain(False)
    r = LogicChain(True)
    result1 = p.and_(q).not_().or_(r).value
    print(result1)
    result2 = q.or_(p.not_()).and_(r.not_()).value
    print(result2)