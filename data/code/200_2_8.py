POSITIVE_THRESHOLD = 0.0

def sum_positive_values(float_list):
    total = 0.0
    for num in float_list:
        if num > POSITIVE_THRESHOLD:
            total += num
    return total

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 4.8, 0.0, -1.1, 3.2]
    result = sum_positive_values(sample_values)
    print(result)