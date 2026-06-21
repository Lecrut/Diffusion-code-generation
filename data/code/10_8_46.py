def calculate_mean(temp1, temp2):
    return (temp1 + temp2) / 2

if __name__ == '__main__':
    temp1 = 23.5
    temp2 = 27.8
    mean_temperature = calculate_mean(temp1, temp2)
    print(f"{mean_temperature:.2f}")