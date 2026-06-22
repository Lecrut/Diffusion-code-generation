def sum_of_integers(*args):
    if len(args) != 6:
        raise ValueError("Exactly six integers are required")
    return sum(args)

if __name__ == '__main__':
    try:
        result = sum_of_integers(-10, -5, 0, 5, 10, 15)
        print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")
    except ValueError as e:
        print(e)