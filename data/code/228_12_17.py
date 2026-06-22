import turtle

def draw_shape(shape_type, side_length):
    shapes = {
        'triangle': 3,
        'square': 4
    }
    sides = shapes.get(shape_type)
    if not sides:
        raise ValueError("Unsupported shape type")

    for _ in range(sides):
        turtle.forward(side_length)
        turtle.left(360 / sides)

if __name__ == '__main__':
    turtle.speed(1)
    draw_shape('triangle', 100)
    turtle.done()