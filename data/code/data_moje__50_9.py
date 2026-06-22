def display_inverted_triangle():
    height = 5
    for row in range(height, 0, -1):
        stars = '*' * row
        print(stars)
    return f"Inverted triangle of height {height} displayed."

if __name__ == '__main__':
    result = display_inverted_triangle()
    print(result)