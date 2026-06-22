def smallest_magnitude_complex(numbers):
    return min(numbers, key=abs)

if __name__ == '__main__':
    sample_numbers = [3 + 4j, 1 - 1j, 2 + 2j]
    print(smallest_magnitude_complex(sample_numbers))