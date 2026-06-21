import heapq

def find_largest_value(numbers):
    if not numbers:
        raise ValueError("Input iterable cannot be empty")
    return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    sample_values = [8, 34, 2, 76, 5, 90, 1]
    print(f"Largest value in {sample_values}: {find_largest_value(sample_values)}")