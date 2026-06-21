if __name__ == '__main__':
    try:
        print(triangle_area(10, 5))
        print(triangle_area(7, 3))
    except ValueError as e:
        print(e)