class BooleanOrChecker:
    def __init__(self, items):
        if not isinstance(items, (list, tuple)):
            raise ValueError("Input must be a list or tuple")
        for item in items:
            if not isinstance(item, bool):
                raise ValueError(f"All items must be booleans, got {type(item)}")
        self.items = tuple(items)

    def has_true(self):
        for item in self.items:
            if item:
                return True
        return False

if __name__ == '__main__':
    my_checker = BooleanOrChecker([False, False, True])
    print(my_checker.has_true())