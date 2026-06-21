def retrieve_extremes(data_sequence):
    if len(data_sequence) < 1:
        raise ValueError("Sequence must contain at least one element")
    head = data_sequence[0]
    tail = data_sequence[-1]
    return head, tail

if __name__ == '__main__':
    raw_text = "99 102 105 108"
    tokens = raw_text.split()
    numeric_values = [int(val) for val in tokens]
    first_val, last_val = retrieve_extremes(numeric_values)
    print(first_val, last_val)