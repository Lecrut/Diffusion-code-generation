def generate_arrowhead(width):
    if width % 2 == 0:
        raise ValueError("Width must be an odd number")
    
    result = ""
    for i in range(1, width + 1, 2):
        result += " " * ((width - i) // 2) + "*" * i + "\n"
    return result

if __name__ == '__main__':
    arrowhead_width = 5
    print(generate_arrowhead(arrowhead_width))