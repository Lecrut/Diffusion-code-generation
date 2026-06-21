def find_max_element(elements):
    if not elements:
        raise ValueError("Input list is empty")
    return max(elements)

if __name__ == '__main__':
    sample_values = [3.5, 1.2, 4.8, 2.9]
    print(find_max_element(sample_values))