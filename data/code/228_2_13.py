import turtle

class EquilateralTriangle:
    side_length = 100
    
    @staticmethod
    def draw():
        angle_step = 2 * 3.14159 / 3
        for _ in range(3):
            turtle.forward(EquilateralTriangle.side_length)
            turtle.left(angle_step)

if __name__ == '__main__':
    EquilateralTriangle.draw()