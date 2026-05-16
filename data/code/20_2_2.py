class Comparator:
    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    c = Comparator()
    obj1 = 10
    obj2 = 10
    obj3 = "hello"
    obj4 = "world"
    print(f"obj1 == obj2: {c.check_equality(obj1, obj2)}")
    print(f"obj1 == obj3: {c.check_equality(obj1, obj3)}")
    print(f"obj3 == obj4: {c.check_equality(obj3, obj4)}")
    print(f"1 == 1: {c.check_equality(1, 1)}")
    print(f"'a' == 'a': {c.check_equality('a', 'a')}")