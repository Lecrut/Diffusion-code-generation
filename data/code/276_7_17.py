class SetRepeater:
    def __init__(self, elements):
        self.elements = set(elements)

    def repeat(self, times):
        repeated_elements = []
        for _ in range(times):
            repeated_elements.extend(list(self.elements))
        return set(repeated_elements)

if __name__ == '__main__':
    repeater = SetRepeater({1, 2, 3})
    result = repeater.repeat(3)
    print(result)