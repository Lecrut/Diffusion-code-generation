def run_length_encode(digits):
    if not digits:
        return []
    encoded = []
    count = 1
    for i in range(1, len(digits)):
        if digits[i] == digits[i - 1]:
            count += 1
        else:
            encoded.append((digits[i - 1], count))
            count = 1
    encoded.append((digits[-1], count))
    return encoded

if __name__ == '__main__':
    sample_sequence = [1, 1, 1, 2, 2, 3, 3, 3, 3, 5]
    result = run_length_encode(sample_sequence)
    print(result)