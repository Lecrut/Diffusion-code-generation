def count_elements(sequence):
    return len([x for x in sequence])
if __name__ == '__main__':
    sample_data = [10, 20, 30]
    result = count_elements(sample_data)
    print(result)