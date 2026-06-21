def extract_third_item(sequence):
    target_index = 2
    retrieved_value = sequence[target_index]
    return retrieved_value

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500]
    output = extract_third_item(sample_data)
    print(output)