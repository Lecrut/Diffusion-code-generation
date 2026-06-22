def rle_encode_case_insensitive(data: str) -> str:
    if not data:
        return ""
    
    lower_data = data.lower()
    result = []
    count = 1
    n = len(lower_data)
    
    for i in range(1, n):
        if lower_data[i] == lower_data[i - 1]:
            count += 1
        else:
            result.append(f"{count}{lower_data[i - 1]}")
            count = 1
    
    result.append(f"{count}{lower_data[n - 1]}")
    
    return "".join(result)

if __name__ == '__main__':
    sample_input = "AaBbCcDDeeff"
    encoded = rle_encode_case_insensitive(sample_input)
    print(encoded)