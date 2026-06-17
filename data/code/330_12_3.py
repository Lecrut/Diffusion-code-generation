class StringModifier:
    @classmethod
    def to_uppercase(cls, instance, attribute_name):
        value = getattr(instance, attribute_name)
        if isinstance(value, str):
            setattr(instance, attribute_name, value.upper())
if __name__ == '__main__':
    class MyStringHolder:
        def __init__(self, text):
            self.text = text
    holder = MyStringHolder("hello world")
    print("Before modification:", holder.text)
    StringModifier.to_uppercase(holder, "text")
    print("After modification:", holder.text)