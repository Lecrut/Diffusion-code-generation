def decode_rle(encoded_list):
    result = []
    for item in encoded_list:
        count = item[0]
        char = item[1]
        result.append(char * count)
    return "".join(result)

if __name__ == "__main__":
    sample_data = [[2, "a"], [3, "b"], [1, "c"]]
    print(decode_rle(sample_data))