def smallest_magnitude_complex(numbers):
    return min(numbers, key=abs)

if __name__ == '__main__':
    sample_values = [3+4j, 1-1j, 2+2j, -1+0j]
    print(smallest_magnitude_complex(sample_values))