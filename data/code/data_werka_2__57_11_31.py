class Geometry:
    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

if __name__ == '__main__':
    base_value = 6
    height_value = 8
    area_result = Geometry.triangle_area(base_value, height_value)
    print(area_result)