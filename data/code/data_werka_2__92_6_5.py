class Inverter:
    def __init__(self, flag):
        if not isinstance(flag, bool):
            raise ValueError("Input must be a boolean")
        self._flag = flag

    def invert(self):
        return not self._flag

    def toggle(self):
        self._flag = not self._flag
        return self._flag

if __name__ == '__main__':
    inv = Inverter(True)
    print(inv.invert())
    print(inv.toggle())
    print(inv.invert())
    try:
        Inverter(1)
    except ValueError as e:
        print(e)