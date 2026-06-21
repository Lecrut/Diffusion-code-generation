def sum_positive_values(float_list):
    total = 0
    for value in float_list:
        if value > 0:
            total += value
    return total

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 4.8, -0.7, 6.2]
    print(sum_positive_values(sample_values))