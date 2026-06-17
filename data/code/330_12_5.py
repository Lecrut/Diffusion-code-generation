class StringModifier:
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
if __name__ == '__main__':
    class MyStringHolder:
        def __init__(self, name):
            self.name = name
            self.data = "hello world"
    holder = MyStringHolder("TestInstance")
    print(f"Before modification: {holder.data}")
    StringModifier.to_uppercase(holder, "data")
    print(f"After modification: {holder.data}")