class StateValidator:
    CRITERIA_A = 0x01
    CRITERIA_B = 0x02
    CRITERIA_C = 0x04
    CRITERIA_D = 0x08

    @staticmethod
    def _evaluate_a(state_flags: int) -> bool:
        return bool(state_flags & StateValidator.CRITERIA_A)

    @staticmethod
    def _evaluate_b(state_flags: int) -> bool:
        return bool(state_flags & StateValidator.CRITERIA_B)

    @staticmethod
    def _evaluate_c(state_flags: int) -> bool:
        return bool(state_flags & StateValidator.CRITERIA_C)

    @staticmethod
    def _evaluate_d(state_flags: int) -> bool:
        return bool(state_flags & StateValidator.CRITERIA_D)

    @classmethod
    def validate(cls, a: bool, b: bool, c: bool, d: bool) -> bool:
        flags = 0
        if a:
            flags |= cls.CRITERIA_A
        if b:
            flags |= cls.CRITERIA_B
        if c:
            flags |= cls.CRITERIA_C
        if d:
            flags |= cls.CRITERIA_D

        if cls._evaluate_a(flags):
            return True
        if cls._evaluate_b(flags) and not cls._evaluate_c(flags):
            return True
        if cls._evaluate_d(flags) and not (cls._evaluate_a(flags) or cls._evaluate_b(flags)):
            return True
        return False

if __name__ == '__main__':
    sample_inputs = [
        (True, False, False, False),
        (False, True, False, False),
        (False, False, True, True),
        (False, False, False, True),
        (False, True, True, False),
        (True, True, True, True)
    ]
    results = [StateValidator.validate(a, b, c, d) for a, b, c, d in sample_inputs]
    print(results)