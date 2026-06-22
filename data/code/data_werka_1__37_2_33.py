class StringCombiner:
    DEFAULT_PREFIX = "Hello"
    DEFAULT_SUFFIX = "World"

    @staticmethod
    def combine(str1, str2):
        return str1 + str2

    @classmethod
    def create_greeting(cls, prefix=DEFAULT_PREFIX, suffix=DEFAULT_SUFFIX):
        return cls.combine(prefix, suffix)

if __name__ == '__main__':
    custom_prefix = "Good morning, "
    custom_suffix = "Earth!"
    greeting = StringCombiner.create_greeting(custom_prefix, custom_suffix)
    print(greeting)