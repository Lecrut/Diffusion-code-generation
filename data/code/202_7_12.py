def find_largest_in_range(start, end):
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    return max(start, end)

if __name__ == '__main__':
    print(f"Largest in range (5, 10): {find_largest_in_range(5, 10)}")
    print(f"Largest in range (-3, -1): {find_largest_in_range(-3, -1)}")
    print(f"Largest in range (20, 20): {find_largest_in_range(20, 20)}")