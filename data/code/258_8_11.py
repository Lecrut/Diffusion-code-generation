def calculate_pair_averages(pair_generator):
    averages = []
    for pair in pair_generator:
        try:
            avg = (pair[0] + pair[1]) / 2
            averages.append(avg)
        except (TypeError, IndexError) as e:
            print(f"Error calculating average for a pair: {e}")
    return tuple(averages)

if __name__ == '__main__':
    sample_pairs = [
        (1, 2),
        (3, 4),
        (5, 6)
    ]
    result = calculate_pair_averages(sample_pairs)
    print(result)