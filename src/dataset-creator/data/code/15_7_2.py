class Settings:
    DEFAULT_ITEMS = ["apple", "banana", "cherry"]
    @staticmethod
    def get_default_items(*args):
        if not args:
            return Settings.DEFAULT_ITEMS
        return args
if __name__ == '__main__':
    print(Settings.get_default_items())
    print(Settings.get_default_items("orange", "grape"))