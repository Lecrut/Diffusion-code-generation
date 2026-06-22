class Rectangle:
    def __init__(self, width=4, height=2):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect_params = {'width': 6, 'height': 3}
    rect = Rectangle(**rect_params)
    print(rect.perimeter())