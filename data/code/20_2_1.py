class Comparator:
    def check_equality(self, a, b):
        return a == b
if __name__ == '__main__':
    c = Comparator()
    obj1 = 10
    obj2 = 10
    obj3 = "hello"
    obj4 = "world"
    obj5 = [1, 2]
    obj6 = [1, 2]
    print(f"obj1 == obj2: {c.check_equality(obj1, obj2)}")
    print(f"obj1 == obj3: {c.check_equality(obj1, obj3)}")
    print(f"obj5 == obj6: {c.check_equality(obj5, obj6)}")