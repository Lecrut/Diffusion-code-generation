SHAPES = {
    "square": lambda s: s * s
}

def calculate_area(shape_name, side_length):
    return SHAPES[shape_name](side_length)

if __name__ == '__main__':
    side = 7
    result = calculate_area("square", side)
    print(result)