def count_elements(sequence):
    counter = 0
    for _ in sequence:
        counter += 1
    return counter
if __name__ == '__main__':
    sample_data = [1, 2, 3, 'a', 'b']
    result = count_elements(sample_data)
    print(result)