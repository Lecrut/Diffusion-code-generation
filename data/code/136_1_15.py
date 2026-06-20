def evaluate_conditions(a: int, b: int, c: int) -> bool:
    ranges = {(0, 10): lambda x, y, z: x < y < z, (10, 20): lambda x, y, z: x > y > z, (20, 30): lambda x, y, z: x == y == z}
    for range_key, condition in ranges.items():
        if range_key[0] <= a < range_key[1]:
            return condition(a, b, c)
if __name__ == '__main__':
    result = evaluate_conditions(5, 10, 15)
    print(result)