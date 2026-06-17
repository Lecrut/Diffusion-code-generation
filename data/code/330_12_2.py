class StringModifier:
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
        else:
            raise TypeError("Attribute must be a string")
class TestClass:
    def __init__(self, name):
        self.name = name
if __name__ == '__main__':
    obj = TestClass("hello world")
    print(f"Before modification: {obj.name}")
    StringModifier.to_uppercase(obj, "name")
    print(f"After modification: {obj.name}")
    obj2 = TestClass("another test")
    print(f"Before modification: {obj2.name}")
    StringModifier.to_uppercase(obj2, "name")
    print(f"After modification: {obj2.name}")