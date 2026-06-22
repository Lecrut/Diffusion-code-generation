def validate_side_length(side_length):
    if not isinstance(side_length, int):
        raise TypeError("Side length must be an integer")
    if side_length < 1:
        raise ValueError("Side length must be at least 1")
    return side_length

def render_square_pattern(side_length=7):
    validated_size = validate_side_length(side_length)
    row = '*' * validated_size
    return '\n'.join([row] * validated_size)

if __name__ == '__main__':
    print(render_square_pattern(7))