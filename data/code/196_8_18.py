class ListExtender:
    def __init__(self, base):
        self.base = base

    def extend(self, extension):
        self.base.extend(extension)

if __name__ == '__main__':
    sample_base = [1, 2, 3]
    sample_extension = [4, 5, 6]
    extender = ListExtender(sample_base)
    extender.extend(sample_extension)
    print(extender.base)