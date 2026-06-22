class DualChecker:
    def __init__(self, val_a, val_b):
        self.a = val_a
        self.b = val_b

    def is_both_false(self):
        return self.a is False and self.b is False

    def is_not_both_true(self):
        return not (self.a is True and self.b is True)

if __name__ == '__main__':
    obj1 = DualChecker(False, False)
    print(obj1.is_both_false())
    
    obj2 = DualChecker(True, False)
    print(obj2.is_both_false())
    
    obj3 = DualChecker(False, True)
    print(obj3.is_both_false())
    
    obj4 = DualChecker(True, True)
    print(obj4.is_both_false())