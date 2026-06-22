MAX_SEQUENCE_LENGTH = 1000

def calculate_sequence_sum(data):
    if not isinstance(data, list) or len(data) > MAX_SEQUENCE_LENGTH:
        raise ValueError("Invalid input: data must be a list of integers with length <= 1000")
    
    try:
        return sum(data)
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_list = [1, 5, 10, 15, 20]
    result = calculate_sequence_sum(sample_list)
    print(result)