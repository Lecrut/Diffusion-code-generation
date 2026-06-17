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
        raise ValueError("Invalid unit specified. Use 'L_to_gal' or 'gal_to_L'")
if __name__ == '__main__':
    liters = 10
    gallons = 3.78541 * liters
    print(f"{liters} liters is equal to {gallons:.4f} gallons")
    gallons_sample = 5
    liters_sample = gallons_sample * 3.78541
    print(f"{gallons_sample} gallons is equal to {liters_sample:.4f} liters")