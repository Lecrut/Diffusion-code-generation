def find_largest_in_range(start, end):
    return max(range(start, end + 1))

if __name__ == '__main__':
    start_value = 3
    end_value = 10
    print(f"Largest in range {start_value} to {end_value}: {find_largest_in_range(start_value, end_value)}")