def sum_eight_elements(tup):
    return tup[0] + tup[1] + tup[2] + tup[3] + tup[4] + tup[5] + tup[6] + tup[7]

if __name__ == '__main__':
    sample_values = (1, 2, 3, 4, 5, 6, 7, 8)
    total_sum = sum_eight_elements(sample_values)
    print(total_sum)