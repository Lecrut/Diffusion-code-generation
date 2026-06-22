conversion_factor = {
    'km_to_miles': 0.621371,
}

def km_to_miles(kilometers: float) -> float:
    return kilometers * conversion_factor['km_to_miles']

if __name__ == '__main__':
    sample_km = 10.0
    print(f"{sample_km} km is equal to {km_to_miles(sample_km):.2f} miles")