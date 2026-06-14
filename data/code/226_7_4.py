def repeat_sequence(num_repetitions):
    result = []
    for _ in range(num_repetitions):
        result.append('A')
        result.append('B')
        result.append('C')
    return result
if __name__ == '__main__':
    repetitions = 12
    final_list = repeat_sequence(repetitions)
    print(final_list)