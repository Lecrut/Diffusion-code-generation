def liters_to_gallons(liters):
    if not isinstance(liters, (int, float)) or liters < 0:
        raise ValueError("Invalid input. Please provide a non-negative number of liters.")
    return liters * 0.264172

if __name__ == '__main__':
    sample_liters = 5
    conversion_factor = liters_to_gallons(sample_liters)
    print(f"{sample_liters} liters is {conversion_factor:.2f} gallons")