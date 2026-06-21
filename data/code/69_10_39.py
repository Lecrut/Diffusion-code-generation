def print_characters_by_indices(s, indices):
    if not isinstance(s, str) or not all(isinstance(i, int) for i in indices):
        raise ValueError("Invalid input types")
    valid_indices = [i for i in indices if 0 <= i < len(s)]
    return ''.join(s[i] for i in valid_indices)

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    sample_indices = [0, 5, 7, 10]
    print(print_characters_by_indices(sample_string, sample_indices))