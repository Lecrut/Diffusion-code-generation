def average_of_tuples(tuples):
    total_sum = 0
    tuple_count = 0
    
    for t in tuples:
        if not isinstance(t, tuple) or len(t) == 0:
            continue
        total_sum += sum(t)
        tuple_count += len(t)
    
    return total_sum / tuple_count if tuple_count > 0 else 0

if __name__ == '__main__':
    sample_data = ((1, 2), (3, 4), (5,))
    print(average_of_tuples(sample_data))