def find_largest_comprehension(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return max(data)

if __name__ == '__main__':
    sample_list_1 = [10, 5, 22, 8, 30]
    sample_list_2 = [-5, -1, -10, -2]
    sample_list_3 = [42]
    print(f"List: {sample_list_1}, Largest: {find_largest_comprehension(sample_list_1)}")
    print(f"List: {sample_list_2}, Largest: {find_largest_comprehension(sample_list_2)}")
    print(f"List: {sample_list_3}, Largest: {find_largest_comprehension(sample_list_3)}")