def min_complex_magnitude(numbers):
    return min(numbers, key=abs)

if __name__ == '__main__':
    sample_numbers = [complex(3, 4), complex(1, 2), complex(5, 12)]
    print(min_complex_magnitude(sample_numbers))