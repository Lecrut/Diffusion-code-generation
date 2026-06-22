import math

class AngleConverter:
    DEGREES_TO_RADIANS = math.pi / 180
    RADIANS_TO_DEGREES = 180 / math.pi
    GRADIANS_TO_RADIANS = math.pi / 200
    RADIANS_TO_GRADIANS = 200 / math.pi

    @staticmethod
    def degrees_to_radians(degrees):
        return degrees * AngleConverter.DEGREES_TO_RADIANS

    @staticmethod
    def radians_to_degrees(radians):
        return radians * AngleConverter.RADIANS_TO_DEGREES

    @staticmethod
    def gradians_to_radians(gradians):
        return gradians * AngleConverter.GRADIANS_TO_RADIANS

    @staticmethod
    def radians_to_gradians(radians):
        return radians * AngleConverter.RADIANS_TO_GRADIANS

if __name__ == '__main__':
    print(AngleConverter.degrees_to_radians(90))
    print(AngleConverter.radians_to_degrees(math.pi))
    print(AngleConverter.gradians_to_radians(400))
    print(AngleConverter.radians_to_gradians(math.pi))