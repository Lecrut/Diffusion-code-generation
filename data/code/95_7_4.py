class AttributeChecker:
    def check_combination(self, obj):
        a = obj.a
        b = obj.b
        c = obj.c
        if a > 0 and b % 2 == 0 and c % a == 0:
            return True
        else:
            return False
if __name__ == '__main__':
    checker = AttributeChecker()
    obj1 = type('Obj1', (object,), {'a': 5, 'b': 10, 'c': 15})()
    obj2 = type('Obj2', (object,), {'a': -2, 'b': 8, 'c': 16})()
    obj3 = type('Obj3', (object,), {'a': 4, 'b': 10, 'c': 12})()
    obj4 = type('Obj4', (object,), {'a': 2, 'b': 7, 'c': 10})()
    print(f"Obj1 result: {checker.check_combination(obj1)}")
    print(f"Obj2 result: {checker.check_combination(obj2)}")
    print(f"Obj3 result: {checker.check_combination(obj3)}")
    print(f"Obj4 result: {checker.check_combination(obj4)}")