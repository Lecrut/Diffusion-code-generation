class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_face_areas(self):
        return [
            self.length * self.width,
            self.width * self.height,
            self.height * self.length
        ]

    def compute_surface_area(self):
        face_areas = self.get_face_areas()
        return 2 * sum(face_areas)

if __name__ == '__main__':
    prism = RectangularPrism(5.0, 3.0, 2.0)
    print(prism.get_face_areas())
    print(prism.compute_surface_area())