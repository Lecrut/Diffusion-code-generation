def dec_to_bin_list(numbers):
    return [bin(num)[2:] for num in numbers]

if __name__ == '__main__':
    sample_values = [10, 25, 128, 3]
    result = dec_to_bin_list(sample_values)
    print(result)