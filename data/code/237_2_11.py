if __name__ == '__main__':
    powers_of_two = {i: 1 << i for i in range(10)}
    for power, value in powers_of_two.items():
        print(f"2^{power} = {value}")