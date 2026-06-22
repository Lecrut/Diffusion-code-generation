def calculate_average(sequence):
    try:
        total = sum(sequence)
        count = len(sequence)
        if count == 0:
            raise ValueError("Sequence cannot be empty")
        average = total / count
        return average
    except TypeError as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_sequence = [100, 200, 300]
    avg = calculate_average(sample_sequence)
    if avg is not None:
        print(avg)