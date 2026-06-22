def fill_rectangle(width, height):
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    return ['#' * width for _ in range(height)]

if __name__ == '__main__':
    try:
        result = fill_rectangle(5, 3)
        print(result)
    except ValueError as e:
        print(e)