class StateValidator:
    _PRINCIPAL_CONDITIONS = {
        'alpha': lambda a, b, c, d: a,
        'beta': lambda a, b, c, d: b and not c,
        'gamma': lambda a, b, c, d: d and not (a or b),
    }

    def __init__(self, a: bool, b: bool, c: bool, d: bool):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def _get_kwargs(self):
        return {
            'a': self.a,
            'b': self.b,
            'c': self.c,
            'd': self.d,
        }

    def validate(self) -> bool:
        kwargs = self._get_kwargs()
        for key, condition in self._PRINCIPAL_CONDITIONS.items():
            if condition(**kwargs):
                return True
        return False

if __name__ == '__main__':
    validator = StateValidator(True, False, False, False)
    print(validator.validate())

    validator2 = StateValidator(False, True, False, False)
    print(validator2.validate())

    validator3 = StateValidator(False, False, True, True)
    print(validator3.validate())

    validator4 = StateValidator(False, False, False, True)
    print(validator4.validate())

    validator5 = StateValidator(False, True, True, False)
    print(validator5.validate())

    validator6 = StateValidator(True, True, True, True)
    print(validator6.validate())