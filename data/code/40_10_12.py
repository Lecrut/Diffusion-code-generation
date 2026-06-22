class RectangularBox:
    LENGTH = 10
    WIDTH = 5
    HEIGHT = 3

    @staticmethod
    def calculate_face_area(a, b):
        return a * b

    @staticmethod
    def surface_area(length, width, height):
        face1 = RectangularBox.calculate_face_area(length, width)
        face2 = RectangularBox.calculate_face_area(width, height)
        face3 = RectangularBox.calculate_face_area(height, length)
        return 2 * (face1 + face2 + face3)

if __name__ == '__main__':
    result = RectangularBox.surface_area(RectangularBox.LENGTH, RectangularBox.WIDTH, RectangularBox.HEIGHT)
    print(result)