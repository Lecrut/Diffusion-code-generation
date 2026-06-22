def generate_line_pattern(length):
    if length <= 0:
        raise ValueError("Length must be a positive integer")
    
    for i in range(length):
        print("*" * (i + 1))

if __name__ == '__main__':
    try:
        generate_line_pattern(5)
    except ValueError as e:
        print(e)