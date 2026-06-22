def calculate_average(number_set):
    total_sum = sum(number_set)
    count = len(number_set)
    if count == 0:
        return 0.0
    return total_sum / count

if __name__ == '__main__':
    sample_sets = [
        {1, 2, 3},
        {4, 5},
        {6, 7, 8, 9}
    ]
    averages = [calculate_average(s) for s in sample_sets]
    print(averages)