class Object:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def is_identical(self, other):
        if not isinstance(other, Object):
            return False
        return self.a == other.a and self.b == other.b
if __name__ == '__main__':
    obj1 = Object(10, "hello")
    obj2 = Object(10, "hello")
    obj3 = Object(20, "world")
    print(f"obj1 is identical to obj2: {obj1.is_identical(obj2)}")
    print(f"obj1 is identical to obj3: {obj1.is_identical(obj3)}")
    obj4 = Object(10, "hello")
    print(f"obj1 is identical to obj4: {obj1.is_identical(obj4)}")