import heapq

def find_largest_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    sample_values = [3, 1, 9, 4, 7]
    print(f"Largest value in {sample_values}: {find_largest_value(sample_values)}")