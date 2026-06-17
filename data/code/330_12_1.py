class StringModifier:
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
        else:
            raise TypeError("Attribute must be a string")
class MyClass:
    def __init__(self, text):
        self.text = text
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
        else:
            raise TypeError("Attribute must be a string")
if __name__ == '__main__':
    obj = MyClass("hello world")
    print(f"Original text: {obj.text}")
    MyClass.to_uppercase(obj, "text")
    print(f"Modified text: {obj.text}")
    obj2 = MyClass("python programming")
    print(f"Original text: {obj2.text}")
    MyClass.to_uppercase(obj2, "text")
    print(f"Modified text: {obj2.text}")