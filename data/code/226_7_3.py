def repeat_sequence():
    result = []
    for i in range(12):
        for j in range(3):
            sequence = ['A', 'B', 'C'][j]
            result.append(sequence)
    return result
if __name__ == '__main__':
    output = repeat_sequence()
    print(output)