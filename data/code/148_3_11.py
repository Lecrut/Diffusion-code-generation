def find_largest(data):
    if not data:
        raise ValueError("List is empty")
    return max(data)

if __name__ == '__main__':
    sample_data = [10, 5, 20, 8]
    print(f"Largest in {sample_data}: {find_largest(sample_data)}")