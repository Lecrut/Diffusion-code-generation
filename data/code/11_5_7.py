EMPTY_RESULT = None

def get_last_item(sequence):
    accumulator = EMPTY_RESULT
    for element in sequence:
        accumulator = element
    return accumulator

if __name__ == '__main__':
    test_values = [10, 20, 30, 40, 50]
    final_value = get_last_item(test_values)
    print(final_value)