def min_complex_magnitude(numbers):
    return min(numbers, key=abs)

if __name__ == '__main__':
    sample_numbers = [3+4j, 1-1j, -2+2j, 0+5j]
    print(min_complex_magnitude(sample_numbers))