if __name__ == '__main__':
    base = 5
    height = 4
    x_coords = [0, base, 0]
    y_coords = [0, 0, height]
    print("Coordinates for the right-angled triangle:")
    for i in range(3):
        print(f"Vertex {i}: ({x_coords[i]}, {y_coords[i]})")