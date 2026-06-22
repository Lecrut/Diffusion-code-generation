class StringNumberValidator:
    def __init__(self, str_a, str_b, str_c, num_x, num_y):
        self.str_a = str_a
        self.str_b = str_b
        self.str_c = str_c
        self.num_x = num_x
        self.num_y = num_y

    def check_string_equality(self):
        return self.str_a == self.str_b

    def check_string_inequality(self):
        return self.str_a != self.str_c

    def check_numerical_inequality(self):
        return self.num_x != self.num_y

    def evaluate_all(self):
        cond1 = self.check_string_equality()
        cond2 = self.check_string_inequality()
        cond3 = self.check_numerical_inequality()
        if cond1 and cond2 and cond3:
            return "Validation passed: all conditions met."
        return "Validation failed: one or more conditions not met."

if __name__ == '__main__':
    validator = StringNumberValidator("hello", "hello", "world", 42, 43)
    print(validator.check_string_equality())
    print(validator.check_string_inequality())
    print(validator.check_numerical_inequality())
    print(validator.evaluate_all())