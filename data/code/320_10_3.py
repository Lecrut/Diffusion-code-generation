def subtract_values(a, b):
    try:
        result = float(a) - float(b)
        return result
    except ValueError:
        raise TypeError("Both inputs must be numeric.")
if __name__ == '__main__':
    print(subtract_values(10.5, 3.2))
    print(subtract_values(20, 5))
    try:
        subtract_values(10, "five")
    except TypeError as e:
        print(f"Error caught: {e}")
    try:
        subtract_values("ten", 5)
    except TypeError as e:
        print(f"Error caught: {e}")