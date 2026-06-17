def compute_sum(a: float, b: float, c: float) -> float:
    return a + b + c
if __name__ == '__main__':
    x = 10.5
    y = -3.2
    z = 4.7
    try:
        result = compute_sum(x, y, z)
        print(f"Sum of {x}, {y}, and {z} is {result}")
    except TypeError as e:
        print(f"Error in computation: {e}")