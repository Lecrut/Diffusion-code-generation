def print_star_square(size):
    if size <= 0:
        print("")
        return ""
    if size == 1:
        line = "*"
        print(line)
        return line
    top_bottom = "*" * size
    middle = "*" + " " * (size - 2) + "*"
    lines = [top_bottom] + [middle] * (size - 2) + [top_bottom]
    output = "\n".join(lines)
    print(output)
    return output

if __name__ == '__main__':
    result = print_star_square(5)
    print(result)
    print("---")
    result = print_star_square(1)
    print(result)
    print("---")
    result = print_star_square(3)
    print(result)