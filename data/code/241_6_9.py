class Geometry:
    LENGTH = 10
    WIDTH = 5

    @staticmethod
    def calculate_area(length, width):
        return length * width

    @classmethod
    def get_sample_area(cls):
        return cls.calculate_area(cls.LENGTH, cls.WIDTH)

if __name__ == '__main__':
    area = Geometry.get_sample_area()
    print(area)