class RectangularBox:
    LENGTH = 10
    WIDTH = 8
    HEIGHT = 6

    @staticmethod
    def area_faces(l, w, h):
        top_bottom = l * w
        front_back = l * h
        left_right = w * h
        return top_bottom + front_back + left_right

    @classmethod
    def surface_area(cls):
        return 2 * cls.area_faces(cls.LENGTH, cls.WIDTH, cls.HEIGHT)

if __name__ == '__main__':
    print(RectangularBox.surface_area())