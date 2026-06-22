def area_of_rectangle(width, height):
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return width * height

def main():
    w_val = 15
    h_val = 7
    res = area_of_rectangle(w_val, h_val)
    print(res)

if __name__ == '__main__':
    main()