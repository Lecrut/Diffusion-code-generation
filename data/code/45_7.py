class GeometryUtils:
    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width
if __name__ == '__main__':
    length_val = 10.0
    width_val = 5.0
    area = GeometryUtils.calculate_area_rectangle(length_val, width_val)
    print(area)