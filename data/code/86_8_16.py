if __name__ == '__main__':
    try:
        a = True
        b = False
        result = (a is not None and b is not None) and a != b
        print(result)
    except TypeError as e:
        print(f"Error: Invalid input. {e}")