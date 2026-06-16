def count_elements(sequence):
    count = 0
    for element in sequence:
        count += 1
    return count
if __name__ == '__main__':
    large_sequence = list(range(1000000))
    result = count_elements(large_sequence)
    print(result)