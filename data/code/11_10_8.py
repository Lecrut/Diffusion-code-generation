def retrieve_final_item(sequence):
    length = len(sequence)
    offset = 1
    index = length - offset
    return sequence[index]

if __name__ == '__main__':
    values = [100, 200, 300, 400, 500]
    output = retrieve_final_item(values)
    print(output)