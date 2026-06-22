class GeometryUtils:
    @staticmethod
    def calculate_area_rectangle(length, width):
        return length * width

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    area = GeometryUtils.calculate_area_rectangle(sample_length, sample_width)
    print(area)