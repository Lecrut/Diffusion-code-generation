class Parallelogram:
    SHAPE = "parallelogram"

    @staticmethod
    def area(base, height):
        return base * height

if __name__ == '__main__':
    print(Parallelogram.area(7, 4))