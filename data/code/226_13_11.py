if __name__ == '__main__':
    sequence = [1, 2, 3]
    num_repeats = 5
    output = []
    
    for _ in range(num_repeats):
        output.extend(sequence)
    
    print(output)