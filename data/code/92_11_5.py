class BooleanFlipper:
    TRUE_VALUES = frozenset(['true', 't', '1', 'yes', 'y'])
    FALSE_VALUES = frozenset(['false', 'f', '0', 'no', 'n'])
    TRUE_STR = 'True'
    FALSE_STR = 'False'

    def __init__(self):
        self.cache = {}

    def _is_true(self, raw: str) -> bool:
        clean = raw.strip().lower()
        if clean in self.cache:
            return self.cache[clean]
        result = clean in self.TRUE_VALUES
        self.cache[clean] = result
        return result

    def flip(self, raw: str) -> str:
        if not isinstance(raw, str):
            raise ValueError("Input must be a string")
        if self._is_true(raw):
            return self.FALSE_STR
        if raw.strip().lower() in self.FALSE_VALUES:
            return self.TRUE_STR
        raise ValueError(f"Invalid boolean string: {raw}")

    def get_opposite(self, raw: str) -> str:
        return self.flip(raw)

if __name__ == '__main__':
    flipper = BooleanFlipper()
    print(flipper.flip('True'))
    print(flipper.flip('False'))
    print(flipper.flip('YES'))
    print(flipper.flip('0'))
    print(flipper.get_opposite('T'))
    print(flipper.get_opposite('F'))