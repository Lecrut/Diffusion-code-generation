if __name__ == '__main__':
    shape = 'O'
    formatted_shape = shape.center(20)
    repeated_shapes = (formatted_shape + '\n') * 20
    print(repeated_shapes.strip())