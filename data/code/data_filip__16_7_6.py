binary_string = "1110011110001"

def run_length_encode(data):
    if not data:
        return []
    counts = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            counts.append(count)
            current_char = data[i]
            count = 1
    counts.append(count)
    return counts

if __name__ == '__main__':
    encoded_result = run_length_encode(binary_string)
    print(encoded_result)