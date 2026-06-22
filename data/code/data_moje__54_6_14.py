def generate_hollow_square(n):
    if n <= 0:
        return ""
    if n == 1:
        return "#"
    top_bottom = "#" + "." * (n - 2) + "#"
    middle = top_bottom
    return (top_bottom + "\n") + (middle + "\n") * (n - 2) + top_bottom

if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)