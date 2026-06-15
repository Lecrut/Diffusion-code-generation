def repeat_sequence(num_repetitions):
    result = []
    for i in range(num_repetitions):
        result.append('A')
        result.append('B')
        result.append('C')
    return result
if __name__ == '__main__':
    n = 12
    output_list = repeat_sequence(n)
    print(output_list)