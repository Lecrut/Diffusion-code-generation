def decimal_to_binary(decimal_list):
    return [bin(d)[2:] if d >= 0 else '-' + bin(d)[3:] for d in decimal_list]

if __name__ == '__main__':
    samples = [0, 5, 10, 255, -10]
    result = decimal_to_binary(samples)
    print(result)