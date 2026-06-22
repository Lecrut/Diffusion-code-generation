def powers_of_two():
    result = []
    for i in range(10):
        power = 1 << i
        result.append(power)
    return result

if __name__ == '__main__':
    print(powers_of_two())