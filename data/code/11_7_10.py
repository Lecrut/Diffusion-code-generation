def retrieve_final_item(sequence):
    if not sequence:
        return None
    iterator = reversed(sequence)
    return next(iterator)

if __name__ == '__main__':
    sample_data = ['red', 'green', 'blue', 'yellow']
    final_value = retrieve_final_item(sample_data)
    print(final_value)