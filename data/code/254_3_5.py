import heapq

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return min(data)

if __name__ == '__main__':
    sample_data = [5, 2, 8, 1, 9]
    print(f"Minimum of {sample_data}: {find_minimum(sample_data)}")