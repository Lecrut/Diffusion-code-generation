import heapq

def find_largest_value(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    return heapq.nlargest(1, numbers)[0]

if __name__ == '__main__':
    sample_list = [3, 1, 9, 4, 7]
    print(f"Max value in {sample_list}: {find_largest_value(sample_list)}")

    sample_tuple = (100, 50, 200, 10)
    print(f"Max value in {sample_tuple}: {find_largest_value(list(sample_tuple))}")

    negative_sample = [-5, -1, -10]
    print(f"Max value in {negative_sample}: {find_largest_value(negative_sample)}")

    empty_list = []
    try:
        find_largest_value(empty_list)
    except ValueError as e:
        print(e)