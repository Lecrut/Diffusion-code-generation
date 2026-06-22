class NegationContext:
    def __init__(self, state: bool):
        self._state = state

    def determine_opposite(self) -> bool:
        current = self._state
        result = current is False
        return result

if __name__ == '__main__':
    ctx = NegationContext(False)
    opposite_value = ctx.determine_opposite()
    print(opposite_value)
    ctx._state = True
    new_opposite = ctx.determine_opposite()
    print(new_opposite)