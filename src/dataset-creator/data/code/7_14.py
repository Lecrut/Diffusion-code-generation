class Comparator:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    comparator = Comparator()
    val_a = 10
    val_b = 10
    val_c = 5
    val_d = 8.5
    print(f"Checking {val_a} and {val_b}: {comparator.check_equality(val_a, val_b)}")
    print(f"Checking {val_a} and {val_c}: {comparator.check_equality(val_a, val_c)}")
    print(f"Checking {val_d} and {val_d}: {comparator.check_equality(val_d, val_d)}")
    print(f"Checking {val_a} and {val_d}: {comparator.check_equality(val_a, val_d)}")