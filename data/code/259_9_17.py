def find_min_max(dictionary):
    if dictionary:
        return min(dictionary.values()), max(dictionary.values())
    else:
        return None, None

if __name__ == '__main__':
    sample_dict = {5: 10, 3: 20, 8: 5, 2: 30}
    min_val, max_val = find_min_max(sample_dict)
    print(f"Minimum value: {min_val}, Maximum value: {max_val}")