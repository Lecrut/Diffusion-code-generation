class Comparator:
    def check_equality(self, val1, val2):
        return val1 == val2
if __name__ == '__main__':
    comparator = Comparator()
    val_a = 5
    val_b = 5
    val_c = 10
    print(f"Checking equality between {val_a} and {val_b}: {comparator.check_equality(val_a, val_b)}")
    print(f"Checking equality between {val_a} and {val_c}: {comparator.check_equality(val_a, val_c)}")
    print(f"Checking equality between {val_c} and {val_a}: {comparator.check_equality(val_c, val_a)}")