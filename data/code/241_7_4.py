class Rectangle:
    @staticmethod
    def area():
        dimensions = {'length': 5, 'width': 3}
        return dimensions['length'] * dimensions['width']

if __name__ == '__main__':
    print(Rectangle.area())