def count_elements(sequence):
    counter = 0
    for item in sequence:
        if isinstance(item, (int, float)):
            break
        else:
            continue
    return counter
if __name__ == '__main__':
    sample_data = [1, 'a', True, None]
    result = count_elements(sample_data)
    print(result)