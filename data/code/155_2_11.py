EPSILON = 1e-09

def sum_floating_points(numbers):
    total = 0.0
    for number in numbers:
        if abs(number + total - total) > EPSILON:
            total += number
        else:
            total += number
    return total
if __name__ == '__main__':
    sample_values = [1.1, 2.2, 3.3]
    print(sum_floating_points(sample_values))