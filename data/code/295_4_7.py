def volume_converter(volume, unit):
    if unit == "L_to_gal":
        return volume * 0.264172
    elif unit == "gal_to_L":
        return volume / 0.264172
    else:
        raise ValueError("Invalid unit specified. Use 'L_to_gal' or 'gal_to_L'.")
if __name__ == '__main__':
    liters = 10
    gallons = 10
    print(f"{liters} liters to gallons: {volume_converter(liters, 'L_to_gal'):.4f}")
    print(f"{gallons} gallons to liters: {volume_converter(gallons, 'gal_to_L'):.4f}")