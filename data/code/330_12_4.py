class StringModifier:
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
        else:
            raise TypeError(f"{attribute_name} must be a string")
class TestClass:
    def __init__(self, name):
        self.name = name
        self.data = "hello world"
if __name__ == '__main__':
    obj = TestClass("TestObject")
    print(f"Before modification: {obj.name}")
    StringModifier.to_uppercase(obj, "name")
    print(f"After modifying 'name': {obj.name}")
    print(f"Original data: {obj.data}")
    obj2 = TestClass("AnotherTest")
    print(f"\nBefore modification: {obj2.data}")
    StringModifier.to_uppercase(obj2, "data")
    print(f"After modifying 'data': {obj2.data}")