def run_length_encode(data):
    if not data:
        return ""
    if len(data) == 1:
        return data[0] + "1"
    result = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            result.append(data[i - 1])
            result.append(str(count))
            count = 1
    result.append(data[-1])
    result.append(str(count))
    return "".join(result)

if __name__ == "__main__":
    sample_input_1 = ""
    sample_input_2 = "a"
    sample_input_3 = "aaabbbcccc"
    sample_input_4 = "AABBCC"
    
    print(run_length_encode(sample_input_1))
    print(run_length_encode(sample_input_2))
    print(run_length_encode(sample_input_3))
    print(run_length_encode(sample_input_4))