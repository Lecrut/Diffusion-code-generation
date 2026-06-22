def mph_to_kmh(mph):
    return mph * 1.60934

if __name__ == '__main__':
    conversion_factor = mph_to_kmh(1)
    print(f"Conversion factor from mph to km/h: {conversion_factor}")