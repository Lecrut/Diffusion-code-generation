if __name__ == '__main__':
    values = {'one': 10, 'two': 5, 'three': 20}
    sorted_sequence = sorted(values.values(), key=lambda x: x)
    print(sorted_sequence)