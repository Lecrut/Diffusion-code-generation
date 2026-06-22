def calculate_sequence_sum(data):
    try:
        return sum(data)
    except TypeError as e:
        raise ValueError(f"Invalid input: {e}")

if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = calculate_sequence_sum(sample_list)
    print(result)