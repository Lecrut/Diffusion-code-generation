def liters_to_gallons(liters):
    return liters * 0.264172

if __name__ == '__main__':
    sample_values = [1, 5, 10, 20]
    for value in sample_values:
        print(f"{value} liters is {liters_to_gallons(value)} gallons")