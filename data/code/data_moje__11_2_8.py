def extract_final_item(sequence):
    sliced_segment = sequence[-1:]
    return sliced_segment[0]

if __name__ == '__main__':
    data_sequence = ["red", "green", "blue", "yellow", "orange"]
    output_value = extract_final_item(data_sequence)
    print(output_value)