def average_pairs(pair_generator):
    return tuple((a + b) / 2 for a, b in pair_generator)

if __name__ == '__main__':
    sample_data = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    
    try:
        result = average_pairs(sample_data)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")