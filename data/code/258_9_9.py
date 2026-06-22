def average_pairs(pair_strings):
    if not pair_strings:
        return []
    
    pairs = [tuple(map(float, pair.split(','))) for pair in pair_strings]
    first_elements = [pair[0] for pair in pairs]
    second_elements = [pair[1] for pair in pairs]
    
    avg_first = sum(first_elements) / len(first_elements)
    avg_second = sum(second_elements) / len(second_elements)
    
    return [avg_first, avg_second]

if __name__ == '__main__':
    sample_data = ['1.0,2.0', '3.0,4.0', '5.0,6.0', '7.0,8.0']
    averages = average_pairs(sample_data)
    print(f"{averages=}")