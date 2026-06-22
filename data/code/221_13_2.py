if __name__ == '__main__':
    values = {1: 20, 2: 5, 3: 10}
    sorted_sequence = sorted(values.values(), key=lambda x: x)
    print(sorted_sequence)