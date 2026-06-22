def is_any_true(data, data_list):
    if not isinstance(data, bool):
        raise ValueError("First argument must be a boolean")
    if not isinstance(data_list, (list, tuple)):
        raise ValueError("Second argument must be a list or tuple")
    for item in data_list:
        if not isinstance(item, bool):
            raise ValueError("All items in the list must be booleans")
    
    class TruthChecker:
        def __init__(self, flag, items):
            self.flag = flag
            self.items = items
        
        def check(self):
            if self.flag:
                return True
            return any(self.items)
    
    checker = TruthChecker(data, data_list)
    return checker.check()

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, True]))
    print(is_any_true(False, [False, False]))