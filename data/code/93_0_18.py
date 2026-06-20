def both_false(x: bool, y: bool) -> bool:
    return not x and not y

if __name__ == '__main__':
    input_x = False
    input_y = True
    result = both_false(input_x, input_y)
    print(result)