class FlipFlop:
    def __init__(self, active: bool):
        self.active = active

    def get_negation(self) -> bool:
        return not self.active

    def reset(self, value: bool) -> None:
        self.active = value

if __name__ == '__main__':
    device = FlipFlop(True)
    print(device.get_negation())
    device.reset(False)
    print(device.get_negation())
    device.reset(True)
    print(device.get_negation())