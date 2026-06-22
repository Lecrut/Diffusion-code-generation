def calculate_average_of_tuples(tuples):
    if not tuples:
        return 0
    
    total_sum = sum(sum(t) for t in tuples)
    total_count = sum(len(t) for t in tuples)
    
    return total_sum / total_count

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5, 6))
    result = calculate_average_of_tuples(sample_data)
    print(result)