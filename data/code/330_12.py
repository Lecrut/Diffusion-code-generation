class StringModifier:
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
        else:
            raise TypeError("Attribute must be a string")
class MyClass:
    def __init__(self, name):
        self.name = name
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
        else:
            raise TypeError("Attribute must be a string")
if __name__ == '__main__':
    obj = MyClass("hello world")
    print(f"Original name: {obj.name}")
    MyClass.to_uppercase(obj, "name")
    print(f"Modified name: {obj.name}")
    obj2 = MyClass("python programming")
    print(f"Original name: {obj2.name}")
    MyClass.to_uppercase(obj2, "name")
    print(f"Modified name: {obj2.name}")