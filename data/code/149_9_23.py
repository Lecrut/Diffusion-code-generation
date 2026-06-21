def validate_list(mixed_list):
    if not isinstance(mixed_list, list):
        raise ValueError("Input must be a list")

def reverse_list(mixed_list):
    validate_list(mixed_list)
    return mixed_list[::-1]

if __name__ == '__main__':
    sample = [42, "world", 2.718, False]
    reversed_sample = reverse_list(sample)
    print(reversed_sample)