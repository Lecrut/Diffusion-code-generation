class StringNumericValidator:
    def __init__(self, primary_string: str, secondary_string: str, comparison_string: str, value_a: int, value_b: int):
        self.primary_string = primary_string
        self.secondary_string = secondary_string
        self.comparison_string = comparison_string
        self.value_a = value_a
        self.value_b = value_b

    def check_string_equality(self) -> bool:
        return self.primary_string == self.secondary_string

    def check_string_inequality(self) -> bool:
        return self.primary_string != self.comparison_string

    def check_numerical_inequality(self) -> bool:
        return self.value_a != self.value_b

    def evaluate_all(self) -> bool:
        cond1 = self.check_string_equality()
        cond2 = self.check_string_inequality()
        cond3 = self.check_numerical_inequality()
        return cond1 and cond2 and cond3

def run_validation():
    val_a = 42
    val_b = 42
    str_x = "alpha"
    str_y = "alpha"
    str_z = "beta"

    validator = StringNumericValidator(str_x, str_y, str_z, val_a, val_b)
    result = validator.evaluate_all()
    return result

if __name__ == '__main__':
    outcome = run_validation()
    print(outcome)