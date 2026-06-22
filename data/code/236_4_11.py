import itertools

class ShapeRepeater:
    def __init__(self, coords):
        self.coords = coords

    def repeat_shape(self, times):
        repeated_coords = list(itertools.chain.from_iterable(itertools.repeat(self.coords, times)))
        return repeated_coords

if __name__ == '__main__':
    sample_coords = [1, 1, 5, 5]
    repeater = ShapeRepeater(sample_coords)
    result = repeater.repeat_shape(3)
    print(result)