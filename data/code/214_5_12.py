def smallest_positive(numbers):
    return min([n for n in numbers if n > 0])

if __name__ == '__main__':
    sample_values = [-5, -2, 3, 1, 4]
    print(smallest_positive(sample_values))