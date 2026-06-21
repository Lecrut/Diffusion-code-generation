def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_list = [15, 23, -7, 0, 42]
    print(f"Smallest in {sample_list}: {find_smallest(sample_list)}")