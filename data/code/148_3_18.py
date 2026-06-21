def find_largest(data):
    if not data:
        raise ValueError("List is empty")
    return max(data)

if __name__ == '__main__':
    sample_data1 = [3, 5, 1, 2, 4]
    print(f"Largest in {sample_data1}: {find_largest(sample_data1)}")

    sample_data2 = [7, -2, 8, 0, 5]
    print(f"Largest in {sample_data2}: {find_largest(sample_data2)}")