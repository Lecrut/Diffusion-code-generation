def liters_to_gallons(liters):
    conversion_factor = 0.264172
    return f"{liters} liters is {liters * conversion_factor:.2f} gallons"

if __name__ == '__main__':
    print(liters_to_gallons(1))
    print(liters_to_gallons(5))