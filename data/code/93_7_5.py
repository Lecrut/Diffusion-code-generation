class DualStateValidator:
    def __init__(self, flag_a: bool, flag_b: bool):
        self.flag_a = flag_a
        self.flag_b = flag_b

    def is_neither_active(self) -> bool:
        return not self.flag_a and not self.flag_b

    def get_status_code(self) -> int:
        if not self.flag_a and not self.flag_b:
            return 0
        if self.flag_a and self.flag_b:
            return 3
        return 1 if self.flag_a else 2

if __name__ == '__main__':
    state = DualStateValidator(False, False)
    print(state.is_neither_active())
    print(state.get_status_code())
    state.flag_a = True
    print(state.is_neither_active())
    print(state.get_status_code())