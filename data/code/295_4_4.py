def volume_converter(volume, unit):
    if unit == "L_to_gal":
        if volume == 0:
            return 0.0
        return volume / 3.78541
    elif unit == "gal_to_L":
        if volume == 0:
            return 0.0
        return volume * 3.78541
    else:
        raise ValueError("Invalid unit specified. Use 'L_to_gal' or 'gal_to_L'.")
if __name__ == '__main__':
    liters = 10
    gallons = 10
    print(f"{liters} liters is equal to {volume_converter(liters, 'L_to_gal'):.4f} gallons")
    print(f"{gallons} gallons is equal to {volume_converter(gallons, 'gal_to_L'):.4f} liters")