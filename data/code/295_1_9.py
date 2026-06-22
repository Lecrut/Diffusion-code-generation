def liters_to_gallons(liters):
    if not isinstance(liters, (int, float)) or liters < 0:
        raise ValueError("Invalid input. Please provide a non-negative number of liters.")
    return f"{liters} liters is {liters * 0.264172:.2f} gallons"

if __name__ == '__main__':
    sample_liters = 5
    print(liters_to_gallons(sample_liters))