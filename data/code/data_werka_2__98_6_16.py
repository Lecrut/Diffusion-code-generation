class ScenarioValidator:
    def __init__(self, str_val_a, str_val_b, str_val_c, num_val_x, num_val_y):
        self.str_val_a = str_val_a
        self.str_val_b = str_val_b
        self.str_val_c = str_val_c
        self.num_val_x = num_val_x
        self.num_val_y = num_val_y

    def evaluate(self):
        str_equal = self.str_val_a == self.str_val_b
        str_unequal = self.str_val_a != self.str_val_c
        num_inequality = self.num_val_x != self.num_val_y
        num_comparison = self.num_val_y > self.num_val_x
        return str_equal and str_unequal and num_inequality and num_comparison

if __name__ == '__main__':
    validator = ScenarioValidator("cherry", "cherry", "date", 20, 30)
    result = validator.evaluate()
    print(result)