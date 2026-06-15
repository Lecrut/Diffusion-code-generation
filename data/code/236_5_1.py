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
    count = 3
    for i in range(count):
        print(f"--- Pattern for {target_shape}, repetition {i + 1} ---")
        for line in pattern_generator:
            print(line)
        print("-" * 20)