if __name__ == '__main__':
    sequence = ['A', 'B', 'C']
    num_repeats = 50
    output = ""
    for _ in range(num_repeats):
        for item in sequence:
            output += item + ", "
    print(output.rstrip(','))