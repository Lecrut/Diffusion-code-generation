def find_max_value(mixed_list):
    if not all(isinstance(x, (int, float)) for x in mixed_list):
        raise ValueError("List must contain only integers and floats")
    return max(mixed_list)

if __name__ == '__main__':
    sample_values = [3, 5.5, 2, 8.9, 1]
    print(find_max_value(sample_values))