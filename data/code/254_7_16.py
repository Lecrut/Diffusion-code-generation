def find_complex_min(complex_list):
    if not complex_list:
        return None
    min_val = min(complex_list, key=abs)
    return min_val

if __name__ == '__main__':
    sample_values = [3+4j, 1-2j, -5+6j, 0-1j]
    result = find_complex_min(sample_values)
    print(result)