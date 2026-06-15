def repeat_sequence():
    result = []
    for i in range(12):
        result.append('A')
        result.append('B')
        result.append('C')
    return result
if __name__ == '__main__':
    output = repeat_sequence()
    print(output)