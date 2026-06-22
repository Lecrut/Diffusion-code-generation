class StateValidator:
    def __init__(self, active: bool, secondary: bool, tertiary: bool, quaternary: bool):
        self.active = active
        self.secondary = secondary
        self.tertiary = tertiary
        self.quaternary = quaternary

    def evaluate(self) -> bool:
        if self.active:
            return self.secondary
        if self.tertiary:
            return not self.quaternary
        return self.active or self.secondary or self.tertiary or self.quaternary

    def get_status_summary(self) -> dict:
        return {
            "active": self.active,
            "secondary": self.secondary,
            "tertiary": self.tertiary,
            "quaternary": self.quaternary,
            "result": self.evaluate()
        }

if __name__ == '__main__':
    validator = StateValidator(True, False, False, True)
    print(validator.evaluate())
    print(validator.get_status_summary())
    
    validator2 = StateValidator(False, False, True, False)
    print(validator2.evaluate())
    print(validator2.get_status_summary())
    
    validator3 = StateValidator(False, False, False, False)
    print(validator3.evaluate())
    print(validator3.get_status_summary())