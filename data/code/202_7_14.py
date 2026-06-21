def find_largest_in_range(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return end

if __name__ == '__main__':
    print(f"Largest in range (10, 20): {find_largest_in_range(10, 20)}")
    print(f"Largest in range (-5, 5): {find_largest_in_range(-5, 5)}")
    print(f"Largest in range (0, 0): {find_largest_in_range(0, 0)}")
    print(f"Largest in range (100, 200): {find_largest_in_range(100, 200)}")