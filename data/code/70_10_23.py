def get_boundary_strings(texts):
    if not texts:
        raise ValueError("Input list cannot be empty")
    first_element = texts[0]
    last_element = texts[-1]
    return first_element, last_element

if __name__ == '__main__':
    sample_data = ["initial", "middle1", "middle2", "final"]
    start, end = get_boundary_strings(sample_data)
    print(start)
    print(end)