def triangular_numbers():
    try:
        return [n * (n + 1) // 2 for n in range(1, 13)]
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == '__main__':
    sample_result = triangular_numbers()
    print(sample_result)