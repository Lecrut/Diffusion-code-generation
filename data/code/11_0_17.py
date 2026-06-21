def fetch_tail(sequence):
    if not sequence:
        raise IndexError("Cannot retrieve tail of an empty sequence")
    return sequence[-1]

def build_test_data():
    return [100, 200, 300, 400, 500]

if __name__ == '__main__':
    test_sequence = build_test_data()
    tail_value = fetch_tail(test_sequence)
    print(tail_value)