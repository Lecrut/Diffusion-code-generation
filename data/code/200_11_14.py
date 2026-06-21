class ElementSelector:
    def __init__(self):
        self.data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def get_alternate_elements(self):
        for i in range(0, len(self.data), 2):
            yield self.data[i]

if __name__ == '__main__':
    selector = ElementSelector()
    gen = selector.get_alternate_elements()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))