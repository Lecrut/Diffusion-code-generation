class BooleanFlux:
    INVERT_MAP = {True: False, False: True}

    def __init__(self, is_active: bool):
        if not isinstance(is_active, bool):
            raise ValueError("Input must be a boolean")
        self.is_active = is_active

    @staticmethod
    def _get_opposite(value: bool) -> bool:
        return BooleanFlux.INVERT_MAP[value]

    def determine_opposite(self) -> bool:
        return self._get_opposite(self.is_active)

    def flip_state(self) -> bool:
        self.is_active = not self.is_active
        return self.is_active

if __name__ == '__main__':
    flux = BooleanFlux(True)
    result = flux.determine_opposite()
    print(result)
    flux.flip_state()
    print(flux.determine_opposite())