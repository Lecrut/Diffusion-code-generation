def shape_pattern_generator(shape):
    if shape == "square":
        yield ["##",
               "#  ",
               "##"]
    elif shape == "triangle":
        yield ["#",
               "##",
               "###"]
    else:
        yield ["Shape not found"]
if __name__ == '__main__':
    target_shape = "square"
    pattern_generator = shape_pattern_generator(target_shape)
    print(f"Pattern for {target_shape}:")
    for _ in range(3):
        for line in pattern_generator:
            print(line)
        print("-" * 5)