def sum_positive_values(float_list):
    total = 0
    for num in float_list:
        if num > 0:
            total += num
    return total

if __name__ == '__main__':
    sample_values = [2.5, -3.6, 7.8, 1.0, -4.5, 0.0]
    result = sum_positive_values(sample_values)
    print(result)